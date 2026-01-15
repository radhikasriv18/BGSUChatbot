import json
import time
import re
from openai import OpenAI
from groq import Groq
from backend.utils.config import OPENROUTER_API_KEY, GROQ_API_KEY, BASE_URL

SYSTEM_PROMPT = """
You are a warm, friendly BGSU student support assistant.

You MUST always respond ONLY in this JSON format:

{
  "reply": "<2–4 warm friendly sentences>",
  "resources": [
    {
      "title": "Resource name",
      "description": "1–2 sentence friendly explanation.",
      "link": "https://example.com"
    }
  ]
}

RULES:
- NEVER reply in plain text.
- NEVER add any text outside of JSON.
- NEVER wrap JSON in backticks.
- MUST return valid JSON only.
- Keep tone warm and supportive.
"""

OPENROUTER_MODELS = [
    "mistralai/mistral-small-3.1-24b-instruct:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "google/gemini-2.0-flash-exp:free",
    "deepseek/deepseek-r1:free"
]


def clean_json_output(raw: str):
    """Extracts JUST JSON from the model output."""
    match = re.search(r"\{[\s\S]*\}", raw)
    if not match:
        raise ValueError("No JSON found")
    return match.group(0)


def call_llm(prompt: str):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt}
    ]

    or_client = OpenAI(base_url=BASE_URL, api_key=OPENROUTER_API_KEY)

    
    for model in OPENROUTER_MODELS:
        try:
            print(f"Trying model: {model}")

            resp = or_client.chat.completions.create(
                model=model,
                messages=messages
            )

            raw = resp.choices[0].message.content
            cleaned = clean_json_output(raw)
            return json.loads(cleaned)

        except Exception as e:
            print(f"Model failed: {model} → {e}")
            time.sleep(1)

    
    print("Fallback → GROQ API")
    groq_client = Groq(api_key=GROQ_API_KEY)

    try:
        gr = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages
        )

        raw = gr.choices[0].message.content
        cleaned = clean_json_output(raw)
        return json.loads(cleaned)

    except Exception as e:
        print("GROQ failed:", e)

        return {
            "reply": "I'm having trouble responding right now — please try again soon.",
            "categories": []
        }
