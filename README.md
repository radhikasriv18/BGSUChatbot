# Student Resource Chatbot

A full-stack AI-powered chatbot application that helps students find relevant resources and get answers to their questions using LLM API.

## Project Overview

This project consists of:

- **Backend**: Python FastAPI server that handles chat requests and resource recommendations
- **Frontend**: React-based web interface with a modern chat UI

The chatbot leverages OpenRouter's API to generate intelligent responses and recommend relevant educational resources.

## Demo

Check out this demo video to see the chatbot in action:

```html
<video width="560" height="315" controls>
  <source src="./media/bgsuchatbot.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>
```

## Tech Stack

### Backend

- **FastAPI** 0.109.0 - Modern web framework for building APIs
- **Uvicorn** 0.27.0 - ASGI server
- **OpenAI** 1.14.0 - OpenRouter API client
- **Pydantic** 2.5.3 - Data validation
- **Python-dotenv** 1.0.0 - Environment variable management

### Frontend

- **React** 19.2.0 - UI library
- **Bootstrap** 5.3.8 - CSS framework
- **Axios** 1.13.2 - HTTP client
- **React Icons** 5.5.0 - Icon library
- **Animate.css** 4.1.1 - CSS animations

## Project Structure

```
newbot/
├── backend/
│   ├── main.py                 # FastAPI application entry point
│   ├── list_models.py          # Available models listing
│   ├── routers/
│   │   └── chat.py            # Chat endpoint
│   ├── schemas/
│   │   └── chat_schema.py      # Request/response schemas
│   ├── services/
│   │   ├── llm.py             # LLM API integration
│   │   └── recommend.py        # Resource recommendation logic
│   └── utils/
│       └── config.py           # Configuration utilities
├── frontend/
│   ├── src/
│   │   ├── App.js             # Main app component
│   │   ├── index.js           # React entry point
│   │   ├── components/
│   │   │   ├── ChatInput.jsx   # Message input component
│   │   │   ├── ChatWindow.jsx  # Chat display component
│   │   │   ├── MessageBubble.jsx # Individual message bubble
│   │   │   └── ResourceCard.jsx # Resource display card
│   │   └── index.css          # Global styles
│   └── public/
├── requirements.txt            # Python dependencies
├── package.json               # Root npm configuration
└── README.md                  # This file
```

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai))

### Backend Setup

1. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Create a `.env` file in the project root:**

   ```env
   OPENROUTER_API_KEY="your key"
   ```

3. **Start the backend server:**
   ```bash
   python -m uvicorn backend.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Install dependencies:**

   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```
   The app will open at `http://localhost:3000`

## Features

- Real-time chat interface
- AI-powered responses using DeepSeek model
- Automatic resource recommendations
- Modern and responsive UI
- Fast and efficient API
- Message history support

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [OpenRouter API Docs](https://openrouter.ai/docs)
- [DeepSeek Model Info](https://openrouter.ai/models)

---
