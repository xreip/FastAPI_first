""" 
Not sure if useful
"""
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.config.config import CONFIG


async def initiate_database():
    client = AsyncIOMotorClient(CONFIG.mongo_uri)
    await init_beanie(database=client.get_default_database(), document_models=[])
