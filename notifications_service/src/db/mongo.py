from beanie import init_beanie # noqa
from src.models.movies import MovieViewStats
from src.models.notifications import NotificationHistory
from src.models.user import User


async def init_db(db):
    """
    Инициализация Beanie с MongoDB.
    """
    await init_beanie(database=db, document_models=[MovieViewStats])
    await init_beanie(database=db, document_models=[NotificationHistory])
    await init_beanie(database=db, document_models=[User])
