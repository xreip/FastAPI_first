"""
FastAPI server configuration
"""
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from pydantic import BaseSettings
from os import getenv

load_dotenv()


class Settings(BaseSettings):
    """Server config settings"""

    # Mongo Engine settings
    mongo_uri = getenv("MONGO_URI")

    # Security settings
    authjwt_secret_key = getenv("JWT_SECRET")
    salt = getenv("SALT").encode()

    # FastMail SMTP server settings
    # mail_console = config("MAIL_CONSOLE", default=False, cast=bool)
    # mail_server = config("MAIL_SERVER", default="smtp.myserver.io")
    # mail_port = config("MAIL_PORT", default=587, cast=int)
    # mail_username = config("MAIL_USERNAME", default="")
    # mail_password = config("MAIL_PASSWORD", default="")
    # mail_sender = config("MAIL_SENDER", default="noreply@myserver.io")

    # testing = config("TESTING", default=False, cast=bool)


CONFIG = Settings()


async def initiate_database():
    client = AsyncIOMotorClient(CONFIG.mongo_uri)
    await init_beanie(database=client.get_default_database(), document_models=[])
