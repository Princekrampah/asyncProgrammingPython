import aiohttp
import asyncio


async def main():
    URL = "https://jsonplaceholder.typicode.com/todos"
    json_body = {
        "title": "first post title",
        "body": "First post content",
        "userId": 20
    }
    headers = {'Content-Encoding': 'deflate'}

    async with aiohttp.ClientSession() as session:
        async with session.post(url=URL, json=json_body, headers=headers) as post_request:
            print(await post_request.text())


asyncio.run(main())
