from datetime import datetime
from typing import Optional
from pydantic import EmailStr, Field, BaseModel
from core.validation import StrippedModel

class ContactCreate(StrippedModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    message: str = Field(..., min_length=1)

class ContactDB(ContactCreate):
    createdAt: datetime = Field(default_factory=datetime.utcnow)

class ContactOut(BaseModel):
    message: str
    id: Optional[str] = None

