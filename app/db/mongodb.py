from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from ..core.config import settings

_client: Optional[AsyncIOMotorClient] = None
_db: Optional[AsyncIOMotorDatabase] = None

async def connect_to_mongo():
    global _client, _db
    try:
        _client = AsyncIOMotorClient(settings.MONGODB_URI)
        _db = _client[settings.DATABASE_NAME]
        # Test connection
        await _client.admin.command('ping')
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        raise

async def close_mongo_connection():
    global _client
    if _client:
        _client.close()
        print("Disconnected from MongoDB")

def get_db() -> AsyncIOMotorDatabase:
    if _db is None:
        raise RuntimeError("Database not initialized. Call connect_to_mongo() first.")
    return _db

def get_contact_collection() -> AsyncIOMotorCollection:
    return get_db()[settings.CONTACT_COLLECTION]

