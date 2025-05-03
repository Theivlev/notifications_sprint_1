from datetime import datetime
from uuid import UUID

from beanie import Document
from pydantic import Field
from src.models.mixins import PyObjectId


class NotificationRecord(Document):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    user_id: UUID
    body: str
    recipient: str
    delivery_method: str
    expiration_time: datetime

    class Settings:
        name = "notification_record"
