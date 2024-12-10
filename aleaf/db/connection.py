from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import errors
from typing import Optional
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from aleaf.core.config import settings
import os
import logging

# Set up logging
logger  = logging.getLogger(__name__)

# Load environment variables (e.g., MongoDB URL) or use defaults
MONGO_DB_URL = settings.MONGO_DB_URL
DB_NAME = settings.DB_NAME

#create the mongoDB cliennt
client = AsyncIOMotorClient(MONGO_DB_URL) #type: ignore

db = client[settings.DB_NAME]

try:
    client.admin.command('ping') #type: ignore
    logger.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

async def connect_db():
    return client
    
def get_collection(collection_name: str):
    """Get a collection from the MongoDB database."""
    if db == None:
        raise Exception("Database not connected.")
    return db[collection_name]

async def close_db():
    """Close the MongoDB connection."""
    client
    if client:
        client.close()
        logger.info("MongoDB connection closed.")