from google.genai import types
from dotenv import load_dotenv
import os
import os
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open('sample_images/image_1.jpg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
model='gemini-2.5-flash',
contents=[
    types.Part.from_bytes(
    data=image_bytes,
    mime_type='image/jpeg',
    ),
    'この画像を日本語で説明して'
]
)

print(response.text)