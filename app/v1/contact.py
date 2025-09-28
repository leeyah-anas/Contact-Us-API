from fastapi import APIRouter, Depends, HTTPException, status
from app.db.mongodb import get_contact_collection
from app.schemas.contact import ContactCreate, ContactOut, ContactDB
from app.services.contact import save_contact

router = APIRouter(tags=["Contact"])

@router.post("/contact", response_model=ContactOut, status_code=201)
async def create_contact(data: ContactCreate, collection=Depends(get_contact_collection)):
    """
    Submit contact form
    
    - **name**: Contact's full name (required, 1-100 chars)
    - **email**: Valid email address (required)
    - **message**: Contact message (required, 1-1000 chars)
    """
    try:
        # Validate input lengths (Pydantic handles basic validation)
        if len(data.name.strip()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"error": "Name cannot be empty"}
                  )
        
        if len(data.message.strip()) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"error": "Message cannot be empty"}
            )
        
        # Create database document
        doc = ContactDB(**data.model_dump())
        contact_id = await save_contact(doc, collection)
        
        return ContactOut(
            message="Contact form submitted successfully", 
            id=contact_id
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "Database connection failed"}
        )