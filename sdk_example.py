# genai sdkを使用した簡易的な例

from google import genai
from dotenv import load_dotenv
import os
from InquirerPy import inquirer
from halo import Halo

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

model_choices=[
    {"name": "gemini-2.5-flash", "value": "gemini-2.5-flash"},
    {"name": "gemini-2.5-flash-lite", "value": "gemini-2.5-flash-lite"},
    {"name": "gemini-2.5-pro", "value": "gemini-2.5-pro"}
]
model = inquirer.select(
    message="選択してください:",
    choices=model_choices,
    default="gemini-2.5-flash",
    pointer="➤",
    instruction="↑↓で移動、Enterで確定",
).execute()

spinner = Halo(text='Thinking...', spinner='dots')

while True:
    request=input("Enter your prompt:")
    spinner.start()
    response = client.models.generate_content(
        model=model,
        contents=request
    )
    spinner.stop()
    print(response.text)
    print('-'*20)
    print(
        f"prompt_token_count: {response.usage_metadata.prompt_token_count}",
        f"candidates_token_count: {response.usage_metadata.candidates_token_count}",
        f"thoughts_token_count: {response.usage_metadata.thoughts_token_count}",
        f"total_token_count: {response.usage_metadata.total_token_count}",
        sep='\n'
    )
