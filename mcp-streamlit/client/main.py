from client import MCPClient
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def main():
    client = MCPClient()
    try:
        path="../server/server.py"
        await client.connect_to_server(path)
        await client.chat_loop()
    finally:
        await client.cleanup()



if __name__ == "__main__":
    asyncio.run(main())    