from src.models.mixins import UUIDMixin


class User(UUIDMixin):
    user_id: str
    first_name: str
    last_name: str | None
    email: str
    tg_id: str | None
    phone_numer: str | None
