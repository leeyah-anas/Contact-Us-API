from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class ContactModel(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    message: str = Field(..., min_length=1)
    createdAt: datetime = Field(default_factory=datetime.utcnow)
