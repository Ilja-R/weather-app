import unittest
from src.model.city_weather import WeatherData, MainData, WindData, CityWeatherData


class TestCityWeatherData(unittest.TestCase):

    def test_city_weather_data_initializes_correctly(self):
        data_str = {"name": "Test City", "weather": [{"main": "Clear", "description": "clear sky"}],
                    "wind": {"speed": 5.5}, "main": {"temp": 293.15, "humidity": 50}}
        data = CityWeatherData(**data_str)
        self.assertEqual(data.name, "Test City")
        self.assertEqual(data.weather[0].main, "Clear")
        self.assertEqual(data.weather[0].description, "clear sky")
        self.assertEqual(data.wind.speed, 5.5)
        self.assertEqual(data.main.temp, 293.15)
        self.assertEqual(data.main.humidity, 50)

    def test_city_weather_data_str_method_formats_correctly(self):
        data = CityWeatherData(
            name="Test City",
            weather=[WeatherData(main="Clear", description="clear sky")],
            wind=WindData(speed=5.5),
            main=MainData(temp=293.15, humidity=50)
        )
        expected_str = (
            "City: Test City\n"
            "    Temperature: 20.0°C\n"
            "    Temperature: 68.0°F\n"
            "    Humidity: 50%\n"
            "    Wind Speed: 5.5 m/s\n"
            "    Weather: clear sky\n"
        )
        self.assertEqual(str(data), expected_str)

    def test_city_weather_data_str_method_formats_correctly_with_missing_data(self):
        data = CityWeatherData(
            name="Test City",
            weather=[WeatherData(main="Clear", description="clear sky")]
        )
        expected_str = (
            "City: Test City\n"
            "    Weather: clear sky\n"
        )
        self.assertEqual(str(data), expected_str)


if __name__ == "__main__":
    unittest.main()
