from fastapi import APIRouter
from backend.services.llm import call_llm

router = APIRouter()

@router.post("/")
def chat(request: dict):
    print("CHAT ENDPOINT HIT")

    message = request.get("message", "")
    data = call_llm(message)

    # Ensuring backend always returns clean JSON
    # Flatten categories into resources if needed for backward compatibility
    resources = data.get("resources", [])
    if not resources and "categories" in data:
        # Flatten nested categories structure
        for cat in data.get("categories", []):
            resources.extend(cat.get("resources", []))
    
    return {
        "reply": data.get("reply", "I'm here to help."),
        "resources": resources
    }
