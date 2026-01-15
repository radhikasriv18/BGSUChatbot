import os
from dotenv import load_dotenv

# Load variables from .env file (recommended)
load_dotenv()

# ============================================================
# API KEYS & MODEL CONFIG
# ============================================================

# Your OpenRouter API Key

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

BASE_URL = "https://openrouter.ai/api/v1"
# Base URL for OpenRouter
BASE_URL = "https://openrouter.ai/api/v1"

# The model you want to use
MODEL_NAME = "gpt-neo-2.7b:free"





# ============================================================
# FALLBACKS (for dev/debug)
# ============================================================

if not OPENROUTER_API_KEY:
    # fallback if .env is not set yet
    OPENROUTER_API_KEY = "YOUR_KEY_HERE"   # replace with your key
