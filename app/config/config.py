"""
FastAPI server configuration
"""
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from rich import print
import sys


class Settings(BaseSettings):
    """Server config settings"""
    JWT_SECRET: str
    MONGO_URI: str
    SALT: str

    # # Mongo Engine settings
    # mongo_uri = getenv("MONGO_URI")

    # # Security settings
    # authjwt_secret_key = getenv("JWT_SECRET")
    # salt = getenv("SALT").encode()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

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
    try:
        client = AsyncIOMotorClient(CONFIG.MONGO_URI)
        await init_beanie(database=client.get_default_database(), document_models=[])
        print(f"Connection success {client}")
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        sys.exit(1)
