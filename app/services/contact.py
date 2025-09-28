from bson import ObjectId  
from motor.motor_asyncio import AsyncIOMotorCollection
from schemas.contact import ContactDB

async def save_contact(contact: ContactDB, collection: AsyncIOMotorCollection) -> str:
    """Save contact to database and return the ID"""
    doc = contact.model_dump()
    result = await collection.insert_one(doc)
    return str(result.inserted_id)
