from pydantic import BaseModel, field_validator

class StrippedModel(BaseModel):
    """Trim whitespace on string fields"""
    @field_validator("*", mode="before")
    @classmethod
    def strip_strings(cls, v):
        return v.strip() if isinstance(v, str) else v
