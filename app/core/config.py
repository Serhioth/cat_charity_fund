import logging
from typing import Optional

from pydantic import BaseSettings, EmailStr

from app.constants import LOGGING_FORMAT


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    description: str = 'Благотворительный фонд поддержки котиков QRKot'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    token_lifetime: int = 3600
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()


def configure_logger() -> logging.Logger:
    """Function for configuring loggers."""

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        LOGGING_FORMAT
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
