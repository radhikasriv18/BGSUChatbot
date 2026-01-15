from openai import OpenAI
from backend.utils.config import OPENROUTER_API_KEY, BASE_URL

client = OpenAI(
    base_url=BASE_URL,
    api_key=OPENROUTER_API_KEY
)

models = client.models.list()

for m in models.data:
    print(m.id)
