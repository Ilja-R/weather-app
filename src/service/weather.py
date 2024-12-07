from dotenv import load_dotenv
import os
import asyncio
import aiohttp
from cachetools import TTLCache

from model.city_weather import CityWeatherData
from exception.weather_exception import WeatherFetchException

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in the environment.")
API = f"https://api.openweathermap.org/data/2.5/weather?q={{city_name}}&appid={API_KEY}"

cache = TTLCache(maxsize=100, ttl=300)

MAX_CONCURRENT_REQUESTS = 10
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)


async def get_weather_from_list(cities: list[str]) -> tuple:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city.lower()) for city in cities]
        return await asyncio.gather(*tasks, return_exceptions=True)


async def fetch_weather(session, city):
    if city in cache:
        return cache[city]

    url = API.format(city_name=city, API_key=API_KEY)
    try:
        async with semaphore:
            async with session.get(url, timeout=10) as response:
                if response.status != 200:
                    raise WeatherFetchException(f"Failed to fetch data. Status code: {response.status}", city,
                                                status_code=response.status, reason=response.reason)
                response_json = await response.json()
                result = CityWeatherData(**response_json)
                cache[city] = result
                return result
    except aiohttp.ClientError as e:
        raise WeatherFetchException(f"Network error: {str(e)}", city)
