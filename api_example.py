from dotenv import load_dotenv
import os
from aiohttp import ClientSession
import asyncio
from halo import Halo

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


async def fetch_gemini_api(api_key,prompt):
    headers = {
        'x-goog-api-key': api_key,
        'Content-Type': 'application/json',
    }

    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        'text': prompt,
                    },
                ],
            },
        ],
    }
    
    async with ClientSession() as session:
        async with session.post(
            "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent",
            headers=headers,
            json=json_data,
            ssl=False
            
        ) as response:
            return await response.json()
            
    

if __name__ == "__main__":
    prompt=input("Enter your prompt:")
    spinner = Halo(text='Thinking...', spinner='dots')
    spinner.start()
    data=asyncio.run(fetch_gemini_api(api_key,prompt))
    spinner.stop()
    print(data["candidates"][0]["content"]["parts"][0]["text"])
