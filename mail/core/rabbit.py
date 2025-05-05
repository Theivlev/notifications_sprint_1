import aio_pika


async def setup_rabbit(connection):
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=10)

    mail_exchange = await channel.declare_exchange("mail_exchange", aio_pika.ExchangeType.DIRECT)
    retry_exchange = await channel.declare_exchange("retry_exchange", aio_pika.ExchangeType.DIRECT)
    failed_exchange = await channel.declare_exchange("failed_exchange", aio_pika.ExchangeType.DIRECT)

    mail_queue = await channel.declare_queue(
        "mail_queue",
        durable=True,
        arguments={
            "x-dead-letter-exchange": "retry_exchange",
            "x-dead-letter-routing-key": "mail",
        },
    )

    retry_queue = await channel.declare_queue(
        "mail_retry_queue",
        durable=True,
        arguments={
            "x-message-ttl": 60000,
            "x-dead-letter-exchange": "mail_exchange",
            "x-dead-letter-routing-key": "mail",
        },
    )

    failed_queue = await channel.declare_queue("failed_queue", durable=True)

    await mail_queue.bind(mail_exchange, routing_key="mail")
    await retry_queue.bind(retry_exchange, routing_key="mail")
    await failed_queue.bind(failed_exchange, routing_key="failed")

    return channel, mail_queue, failed_queue
