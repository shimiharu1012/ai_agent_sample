# genai sdkを使用した簡易的な例

from google import genai
from dotenv import load_dotenv
import os
from InquirerPy import inquirer

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model_choices=[
    {"name": "gemini-2.5-flash", "value": "gemini-2.5-flash"},
    {"name": "gemini-2.5-flash-image", "value": "gemini-2.5-flash-image"},
    {"name": "imagen-4.0-generate-001", "value": "imagen-4.0-generate-001"},
    {"name": "gemini-2.5-pro-exp-01-21", "value": "gemini-2.5-pro-exp-01-21"}
]
model = inquirer.select(
    message="選択してください:",
    choices=model_choices,
    default="gemini-2.5-flash",
    pointer="➤",
    instruction="↑↓で移動、Enterで確定",
).execute()

print(model)

while True:
    request=input("Enter your prompt:")
    response = client.models.generate_content(
        model=model,
        contents=request
    )
    print(response.text)
    print('-'*20)
    print(
        f"prompt_token_count: {response.usage_metadata.prompt_token_count}",
        f"candidates_token_count: {response.usage_metadata.candidates_token_count}",
        f"thoughts_token_count: {response.usage_metadata.thoughts_token_count}",
        f"total_token_count: {response.usage_metadata.total_token_count}",
        sep='\n'
    )
