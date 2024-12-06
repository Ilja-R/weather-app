from dotenv import load_dotenv
import os
import asyncio
import aiohttp
import cache

load_dotenv()

API = "https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in the environment.")

weather_cache = cache.ExpireCache()


async def get_weather(cities: list[str]) -> tuple:
    async with aiohttp.ClientSession() as session:
        tasks = [get_weather(session, city.lower()) for city in cities]
        results = await asyncio.gather(*tasks)
        return results


async def get_weather(session, city: str) -> dict:
    from_cache = weather_cache.get_non_expired(city)
    if from_cache:
        return from_cache
    data = await fetch_weather(session, city)
    if 'error' not in data:
        weather_cache.set(city, data)
    return data


async def fetch_weather(session, city):
    url = API.format(city_name=city, API_key=API_KEY)
    try:
        async with session.get(url, timeout=10) as response:
            if response.status != 200:
                return {
                    "key": city,
                    "status_code": response.status,
                    "reason": response.reason,
                    "error": f"Failed to get weather for key {city}"
                }
            response_json = await response.json()
            return extract(response_json, city)
    except aiohttp.ClientError as e:
        return {"key": city, "error": f"Network error: {str(e)}"}
    except Exception as e:
        return {"key": city, "error": f"Unexpected error: {str(e)}"}


def extract(data: dict, city_name: str) -> dict:
    city_name = data.get("name", city_name)
    temp_kelvin = data['main']['temp']
    temp_celsius = get_celsius_from_kalvin(temp_kelvin)
    temp_fahrenheit = get_fahrenheit_from_celsius(temp_celsius)
    weather_description = data['weather'][0]['description']
    humidity = data['main'].get('humidity', 'N/A')
    wind_speed = data['wind'].get('speed', 'N/A')
    return {"key": city_name, "temp_fahrenheit": temp_fahrenheit, "temp": temp_celsius,
            "description": weather_description,
            "humidity": humidity, "wind_speed": wind_speed}


def get_celsius_from_kalvin(temp_kelvin: float) -> float:
    return round(temp_kelvin - 273.15, 2)


def get_fahrenheit_from_celsius(temp_celsius: float) -> float:
    return round((temp_celsius * 9 / 5) + 32, 2)
