from pydantic import BaseModel, model_validator
from typing import Optional
from helper.unit_converter import get_celsius_from_kalvin, get_fahrenheit_from_kalvin


class CityWeatherData(BaseModel):
    city_name: str
    temp_c: Optional[float] = None
    temp_f: Optional[float] = None
    humidity: Optional[int] = None
    wind_speed: Optional[float] = None
    weather_description: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def transform_input(cls, values):
        transformed = {'city_name': values.get('name')}
        if "main" in values:
            transformed["temp_c"] = get_celsius_from_kalvin(values["main"]["temp"])
            transformed["temp_f"] = get_fahrenheit_from_kalvin(values["main"]["temp"])
            transformed["humidity"] = values["main"]["humidity"]
        if "wind" in values:
            transformed["wind_speed"] = values["wind"]["speed"]
        if "weather" in values:
            transformed["weather_description"] = values["weather"][0]["description"]
        return transformed

    def __str__(self):
        data = "City: " + self.city_name
        if self.temp_c is not None:
            data += "\n    Temperature: " + str(self.temp_c) + " °C"
        if self.temp_f is not None:
            data += "\n    Temperature: " + str(self.temp_f) + " °F"
        if self.humidity is not None:
            data += "\n    Humidity: " + str(self.humidity) + " %"
        if self.wind_speed is not None:
            data += "\n    Wind Speed: " + str(self.wind_speed) + " m/s"
        if self.weather_description is not None:
            data += "\n    Weather Description: " + self.weather_description
        data += "\n"
        return data
