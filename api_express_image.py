from dotenv import load_dotenv
import os
from aiohttp import ClientSession
import asyncio
from halo import Halo
import base64

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
            
async def express_image(api_key,prompt,image_path):
    with open(image_path, 'rb') as f:
      base64_image = base64.b64encode(f.read()).decode('utf-8')

    headers = {
        'x-goog-api-key': api_key,
        'Content-Type': 'application/json',
    }

    json_data = {
        'contents': [
            {
                'parts': [
                    {
                        "inline_data": 
                        {
                            "mime_type":"image/jpeg",
                            "data": base64_image
                        }
                    },
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
    data=asyncio.run(express_image(api_key,prompt,'sample_images/image_2.jpeg'))
    spinner.stop()
    print(data["candidates"][0]["content"]["parts"][0]["text"])
