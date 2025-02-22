from fastapi import FastAPI
from app.config import settings
from app.routes.ocr import router as ocr_router

app = FastAPI(
    title=settings.project_name,
    version="1.0.0",
    debug=settings.debug
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Handwritten Recognition API"}

# Include the OCR router under the '/ocr' prefix
app.include_router(ocr_router, prefix="/ocr")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=settings.host, port=settings.port, reload=settings.debug)
