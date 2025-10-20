"""Application configuration - Hidden from users"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Application configuration"""
    
    # API Settings (OpenRouter)
    API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    API_TYPE = "openrouter"  # Fixed to openrouter
    DEFAULT_MODEL = "deepseek/deepseek-chat-v3.1:free"
    MODEL_NAME = DEFAULT_MODEL  # Alias for compatibility
    API_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    
    # Model settings
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "50000"))
    
    # Available models (backup options if needed)
    MODELS = [
        "deepseek/deepseek-chat-v3.1:free"
    ]
    
    # UI Settings
    DOMAINS = [
        "Research & Analysis",
        "Creative Writing",
        "Technical/Coding",
        "Business Strategy",
        "Education & Teaching",
        "Data Science",
        "General Purpose"
    ]
    
    COMPLEXITY_LEVELS = ["Proficient", "Expert", "Master"]
    
    # App metadata
    APP_NAME = "PromptLab Pro"
    APP_VERSION = "1.0"
    APP_ICON = "🧪"