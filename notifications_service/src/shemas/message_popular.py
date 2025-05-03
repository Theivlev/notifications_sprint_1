from uuid import UUID
from typing import Literal, List, Dict
from src.models.dto import AbstractDTO
import uuid


class MessagePopularMoviesDTO(AbstractDTO):
    id: UUID
    user_id: str
    body: str
    recipient: str
    channel: Literal["email", "push"]
    movies: List[Dict[str, str]]
    notification_type: str = "popular_movies"

    @staticmethod
    def create(user_data: dict, channel: str = 'email') -> "MessagePopularMoviesDTO":
        """
        Создает объект MessagePopularMoviesDTO на основе данных.
        """
        try:
            if not all(key in user_data for key in ["user_id", "email", "movies"]):
                raise ValueError("В user_data отсутствуют обязательные поля: user_id, email, movies")
            body = "У вас новые рекомендации фильмов!"

            return MessagePopularMoviesDTO(
                    id=uuid.uuid4(),
                    user_id=user_data.get("user_id"),
                    body=body,
                    recipient=user_data.get("email"),
                    channel=channel,
                    movies=user_data.get("movies", []),
                    notification_type="popular_movies"
                )
        except Exception as e:
            raise ValueError(f"Ошибка при создании MessagePopularMoviesDTO: {str(e)}")