from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import io
from app.models.ocr import ocr_model

router = APIRouter()

@router.post("/predict", summary="Generate OCR transcription from an image")
async def predict(file: UploadFile = File(...)):
    # Validate file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image.")
    
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert("RGB")
        # Optional: Resize image if necessary (e.g., image = image.resize((384, 384)))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {e}")
    
    # Get prediction from the fine-tuned model
    prediction = ocr_model.predict(image)
    return {"prediction": prediction}
