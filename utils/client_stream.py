import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from mcp.client.streamable_http import streamablehttp_client


class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
    
    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server

        Args:
            server_script_path: Path to the server script (.py or .js)
        """

        command = "python" 
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )

        stdio_transport = await self.exit_stack.enter_async_context(streamablehttp_client("http://127.0.0.1:8000/mcp"))
        self.stdio, self.write,_ = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))

        await self.session.initialize()


    async def process_query(self, query: str) -> str:
        """Process a query using Claude and available tools"""
       
        response = await self.session.list_tools()
        # available_tools = [{
        #     "name": tool.name,
        #     "description": tool.description,
        #     "input_schema": tool.inputSchema
        # } for tool in response.tools]

        # print(available_tools)

        result = await self.session.call_tool('sum', { "a": 2, "b": 2 })
    
        return result.content[0].text  # or result.content or result["output"]


    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()

                if query.lower() == 'quit':
                    break

                response = await self.process_query(query)
                print("\n" + response)

            except Exception as e:
                print(f"\nError: {str(e)}")

    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

async def main():
    client = MCPClient()
    try:
        await client.connect_to_server("./json_data/server.py")
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    import sys
    asyncio.run(main())
                

