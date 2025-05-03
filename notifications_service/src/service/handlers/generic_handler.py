from typing import ClassVar

from src.service.handlers.base import BaseHandler
from src.shemas.delivery import DeliveryDTO


class GenericHandler(BaseHandler):
    notification: ClassVar[str] = "generic"

    async def create_tasks(self, delivery_data: DeliveryDTO) -> None:
        pass
