import asyncio
import aiohttp
import aiofiles
from decouple import config

# Load in API keys
ELEVEN_LABS_API_KEY = config("ELEVENLABS_API_KEY")


async def convert_text_to_speech(message: str, speaker: str):
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0
        }
    }

    speakers: dict = {
        "bella": "EXAVITQu4vr4xnSDxMaL",
        "rachel": "21m00Tcm4TlvDq8ikWAM",
        "antoni": "ErXwobaYiN019PkySvjV",
        "elli": "MF3mGyEYCl7XYWbV9V6O",
        "josh": "TxGEqnHWrfWFTfGW9XjX",
        "anold": "VR6AewLTigWG4xSOukaG",
        "adam": "pNInz6obpgDQGcFmaJgB",
        "sam": "yoZ06aMxZJJ28mfd3POQ"
    }

    voice_id = speakers.get(speaker)

    # Construct request headers and url
    headers = {"xi-api-key": ELEVEN_LABS_API_KEY,
               "Content-Type": "application/json", "accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=endpoint, headers=headers, json=body) as response:
                if response.status == 200:
                    async with aiofiles.open("test.wav", "wb") as file:
                        empty_byte = b""
                        result = empty_byte
                        while True:
                            chunk = await response.content.read(1024)
                            # To determine the EOF
                            if chunk == b"":
                                break
                            result += chunk

                        await file.write(result)
                        print("Done")
                else:
                    return
    except Exception as e:
        print(e)
        return


asyncio.run(convert_text_to_speech(message="Hello world, I love Python programming. What about you?", speaker="anold"))
