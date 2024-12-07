from pydantic import BaseModel
from typing import Optional
from helper.weather_helper import get_celsius_from_kalvin, get_fahrenheit_from_kalvin


class WeatherData(BaseModel):
    main: str
    description: str


class MainData(BaseModel):
    temp: Optional[float] = None
    humidity: Optional[int] = None


class WindData(BaseModel):
    speed: Optional[float] = None


class CityWeatherData(BaseModel):
    name: str
    weather: Optional[list[WeatherData]] = None
    wind: Optional[WindData] = None
    main: Optional[MainData] = None

    def __str__(self):
        data = "City: " + self.name
        if self.main:
            if self.main.temp:
                data += f"\n    Temperature: {get_celsius_from_kalvin(self.main.temp)}°C"
                data += f"\n    Temperature: {get_fahrenheit_from_kalvin(self.main.temp)}°F"
            data += f"\n    Humidity: {self.main.humidity}%"
        if self.wind:
            data += f"\n    Wind Speed: {self.wind.speed} m/s"
        if self.weather:
            data += f"\n    Weather: {self.weather[0].description}"
        data += "\n"
        return data
