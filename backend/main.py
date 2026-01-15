from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers.chat import router as chat_router


app = FastAPI(
    title="Student Resource Chatbot API",
    description="Backend API for chatbot using OpenRouter + DeepSeek",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "API is running!"}
