from src.models.mixins import UUIDMixin


class MovieViewStats(UUIDMixin):
    title: str
    watched_count: int
    movies_in_category: int
    genre: str
