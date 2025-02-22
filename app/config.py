from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    project_name: str = "Handwritten Recognition"
    debug: bool = True
    model_path: str = "path/to/your/model"  # will Update this when the model is ready
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"  # Environment variables

settings = Settings()
