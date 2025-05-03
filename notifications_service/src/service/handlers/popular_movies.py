from typing import ClassVar

from src.service.handlers.base import BaseHandler
from src.shemas.delivery import DeliveryDTO


class PopularMoviesHandler(BaseHandler):
    notification: ClassVar[str] = "popular_movies"

    async def create_tasks(self, delivery_data: DeliveryDTO) -> None:
        pass
