from dataclasses import dataclass
from typing import Any, TypeVar, Type, ClassVar
from src.shemas.delivery import DeliveryDTO
from src.crud.base import BaseMongoCRUD
from models.notifications import NotificationHistory


@dataclass
class NotificationsService:
    producer: Any
    notification_history: BaseMongoCRUD[NotificationHistory]

    async def get_history(self, user_id: str) -> list[dict]:
        history_records = await self.notification_history.find(
            filter_={'user_id': user_id},
            page_number=0,
            page_size=100
        )
        return [NotificationHistory.model_validate(record) for record in history_records]
