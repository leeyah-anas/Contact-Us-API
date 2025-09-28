from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from v1.contact import router as contact_router   # good
from db.mongodb import connect_to_mongo, close_mongo_connection

app = FastAPI(title="VinoVibe Contact API", version="1.0.0")

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"error": "Invalid input", "details": exc.errors()})

app.include_router(contact_router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "ok"}
