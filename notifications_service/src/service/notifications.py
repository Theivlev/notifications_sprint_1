from dataclasses import dataclass
from typing import Any
from src.shemas.delivery import DeliveryDTO # noqa
from src.crud.base import BaseMongoCRUD
from models.notifications import NotificationRecord
from src.shemas.delivery import DeliveryDTO # noqa


@dataclass
class NotificationsService:
    producer: Any
    notification_history: BaseMongoCRUD = BaseMongoCRUD(NotificationRecord)

    async def get_history(self, filter_: dict, page_number: str, page_size: str) -> list[dict]:
        history_records = await self.notification_history.find(
            filter_=filter_,
            page_number=page_number,
            page_size=page_size
        )
        return history_records

    async def notification(self, delivery_data: DeliveryDTO) -> None:
        pass


def get_notifications_service() -> NotificationsService:
    return NotificationsService(
        producer=...,
    )
