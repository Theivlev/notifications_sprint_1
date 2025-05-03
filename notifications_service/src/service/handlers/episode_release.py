from typing import ClassVar

from src.service.handlers.base import BaseHandler
from src.shemas.delivery import DeliveryDTO


class EpisodeReleaseHandler(BaseHandler):
    notification: ClassVar[str] = "episode_release"

    async def create_tasks(self, delivery_data: DeliveryDTO) -> None:
        pass
