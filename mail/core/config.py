import logging

from pydantic_settings import BaseSettings, SettingsConfigDict


class RabbitMQSettings(BaseSettings):
    """Настройки RabbitMQ."""

    host: str
    user: str
    password: str
    port: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="RABBITMQ_")


class GRPCSettings(BaseSettings):
    """Настройки для подключения к gRPC серверу."""

    auth_host: str
    auth_port: int

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="GRPC_")


class SMTPSettings(BaseSettings):
    """Настройки SMTP."""

    host: str
    port: int
    user: str
    password: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore", env_prefix="SMTP_")


rabbit_settings = RabbitMQSettings()  # type: ignore
grpc_settings = GRPCSettings()  # type: ignore
smtp_settings = SMTPSettings()  # type: ignore

# Настройки логирования
LOGGER_FORMAT = "%(asctime)s [%(levelname)s] - %(message)s"
LOGGER_SETTINGS = {
    "level": logging.INFO,
    "format": LOGGER_FORMAT,
    "handlers": [
        logging.StreamHandler(),
    ],
}
logging.basicConfig(**LOGGER_SETTINGS)

TEMPLATES_DIR = "templates"
