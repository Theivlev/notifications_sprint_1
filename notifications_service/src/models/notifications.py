from src.models.mixins import UUIDMixin


class NotificationHistory(UUIDMixin):
    user_id: str
    body: str
    recipient: str
    delivery_method: str
    expiration_time: str
