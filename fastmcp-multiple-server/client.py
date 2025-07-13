import asyncio
from fastmcp import Client


client = Client("./server.py")

async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        resources = await client.list_resources()

        print("Available tools:", tools)
        print("Available resources:", resources)

        print("\n")

        app_status = await client.call_tool("check_app_status", {})

        print("App Status:", app_status.content[0].text)
        
        weather_forecast = await client.call_tool("weather_get_weather_forecast", {"location": "Kolkata"})
            
        print("Weather at Kolkata: ", weather_forecast.content[0].text)

        current_weather_data = await client.read_resource("weather://weather/forecast")

        print("Current weather data:", current_weather_data[0].text)

        news_headlines = await client.call_tool("news_get_news_headlines", {})
            
        print("News headlines: ", news_headlines.content[0].text)

        latest_news_data = await client.read_resource("news://news/headlines")

        print("Latest News data:", latest_news_data[0].text)


asyncio.run(main())