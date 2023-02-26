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

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


CONFIG = Settings()


async def initiate_database():
    try:
        client = AsyncIOMotorClient(CONFIG.MONGO_URI)
        await init_beanie(database=client.get_default_database(), document_models=[])
        print(f"Connection success {client}")
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        sys.exit(1)
