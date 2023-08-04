# pip install aiohttp
import aiohttp
import asyncio


async def main():
    # use context-manager so we do not have to manually
    # remember to close session
    async with aiohttp.ClientSession() as session:
        async with session.get("http://python.org") as response:
            print(response)
            print("\n\n\n")
            print("==================================")
            print(f"Status: {response.status}")
            print(f"Content-type: {response.headers.get('Content-Type')}")

            html = await response.text()
            print("==================================")
            print(f"Body: \n{html}")
    
if __name__ == "__main__":
    asyncio.run(main())