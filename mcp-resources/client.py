import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def main():
    url = "http://127.0.0.1:8000/mcp"
    async with streamablehttp_client(url) as (read, write, get_session_id):
        async with ClientSession(read, write) as session:

            # initialize session
            await session.initialize()

            #list all resources
            resources = await session.list_resources()
            for resource in resources.resources:
                print("Resource with name: "+resource.name+", "+"uri "+str(resource.uri)+", description "+resource.description)
                

            resources = await session.list_resource_templates()
            for resource in resources.resourceTemplates:
                print("Resource with name "+resource.name+", uri "+resource.uriTemplate+", description "+resource.description)
  

            # read resources
            result = await session.read_resource(uri="msg:/greeting/hello")
            print(result.contents[0].text)


            path=r"file://documents/mcp-doc"
            result = await session.read_resource(path)
            print(result.contents[0].text)
           
            path=r"file://documents/hr-doc"
            result = await session.read_resource(path)
            print(result.contents[0].text)
            


if __name__ == "__main__":
    asyncio.run(main())
 