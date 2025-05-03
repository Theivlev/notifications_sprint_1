from typing import ClassVar

from src.service.handlers.base import BaseHandler
from src.shemas.delivery import DeliveryDTO


class UserRegisteredHandler(BaseHandler):
    notification: ClassVar[str] = "user_registered"

    async def create_tasks(self, delivery_data: DeliveryDTO) -> None:
        pass
