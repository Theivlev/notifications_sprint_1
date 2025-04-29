from src.models.dto import AbstractDTO


class User(AbstractDTO):
    user_id: str
    first_name: str
    last_name: str | None
    email: str
    tg_id: str | None
    phone_numer: str | None