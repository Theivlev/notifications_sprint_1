import logging
from smtplib import SMTPException

import aio_pika
from aio_pika.abc import AbstractChannel, AbstractIncomingMessage
from schemas.rabbit import EmailMessage
from services.smtp import send_email_smtp
from services.user import GRPCAuthClient

logger = logging.getLogger(__name__)


async def on_message(message: AbstractIncomingMessage, channel: AbstractChannel):
    failed_exchange = await channel.get_exchange("failed_exchange")

    async with message.process(ignore_processed=True):
        try:
            data = EmailMessage.model_validate(message.body)

            grpc_client = GRPCAuthClient()

            user = await grpc_client.get_user_info(user_id=data.user_id)
            await send_email_smtp(
                email=user.email,
                subject=data.subject,
                template=data.template,
                data={"full_name": f"{user.name} {user.surname}", "subject": data.subject},
            )
            logger.info("Письмо успешно отправлено.")

        except SMTPException as e:
            logger.error(f"Временная SMTP-ошибка: {e}, отправляем в DLX")
            await message.reject(requeue=False)

        except Exception as e:
            logger.error(f"Ошибка при отправке письма: {e}")
            await failed_exchange.publish(
                aio_pika.Message(body=message.body, delivery_mode=aio_pika.DeliveryMode.PERSISTENT),
                routing_key="failed",
            )
            await message.ack()


async def on_failed_message(message: AbstractIncomingMessage):
    async with message.process():
        failed_data = message.body.decode()
        logger.error(f"Письмо не отправлено: {failed_data}")
