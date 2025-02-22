# models/ocr.py

from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch


MODEL_DIR = r"E:\Capstone\handwritten-recognition\handwritten-recognition\trocr-finetuned-less-dataset"

class OCRModel:
    def __init__(self):
        # Choose device: GPU if available, otherwise CPU.
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # Load the fine-tuned TrOCR model and processor from the specified directory.
        self.model = VisionEncoderDecoderModel.from_pretrained(MODEL_DIR).to(self.device)
        self.processor = TrOCRProcessor.from_pretrained(MODEL_DIR)
    
    def predict(self, image: Image.Image) -> str:
        """
        Preprocess the input image, run it through the model,
        and decode the output to generate the transcription.
        """
        # Preprocess the image using the processor.
        pixel_values = self.processor(images=image, return_tensors="pt").pixel_values.to(self.device)
        
        # Generate predictions (token IDs) from the model.
        generated_ids = self.model.generate(pixel_values)
        
        # Decode the generated token IDs to a string.
        transcription = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return transcription

# Instantiate the OCRModel to be used in your FastAPI routes.
ocr_model = OCRModel()
