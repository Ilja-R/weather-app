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

# Set cache time to 10 minutes by default, which seems reasonable for weather data
# Can be changed by setting CACHE_TIME_SECONDS in the environment
CACHE_TIME = int(os.getenv("CACHE_TIME_SECONDS", 600))
# Set max concurrent requests to 10 by default
MAX_CONCURRENT_REQUESTS = int(os.getenv("MAX_CONCURRENT_REQUESTS", 10))

cache = TTLCache(maxsize=100, ttl=CACHE_TIME)
semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)


async def get_weather_from_list(cities: list[str]) -> tuple[CityWeatherData | WeatherFetchException]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city.lower()) for city in cities]
        return await asyncio.gather(*tasks, return_exceptions=True)


async def fetch_weather(session: aiohttp.ClientSession, city: str) -> CityWeatherData | WeatherFetchException:
    if city in cache:
        return cache[city]

    url = API.format(city_name=city, API_key=API_KEY)
    try:
        async with semaphore:
            async with session.get(url, timeout=10) as response:
                if response.status != 200:
                    raise WeatherFetchException(f"Failed to fetch data.", city,
                                                status_code=response.status, reason=response.reason)
                response_json = await response.json()
                result = CityWeatherData.model_validate(response_json)
                cache[city] = result
                return result
    except aiohttp.ClientError as e:
        raise WeatherFetchException(f"Network error: {str(e)}", city)
