import unittest
from src.model.city_weather import CityWeatherData


class TestCityWeatherData(unittest.TestCase):

    def test_city_weather_data_initializes_correctly(self):
        data_str = {"name": "Test City", "weather": [{"description": "clear sky"}],
                    "wind": {"speed": 5.5}, "main": {"temp": 293.15, "humidity": 50}}
        data = CityWeatherData.model_validate(data_str)
        self.assertEqual(data.city_name, "Test City")
        self.assertEqual(data.weather_description, "clear sky")
        self.assertEqual(data.wind_speed, 5.5)
        self.assertEqual(data.temp_c, 20.0)
        self.assertEqual(data.temp_f, 68.0)
        self.assertEqual(data.humidity, 50)

    def test_city_weather_data_initializes_correctly_with_missing_data(self):
        data_str = {"name": "Test City", "weather": [{"description": "clear sky"}]}
        data = CityWeatherData.model_validate(data_str)
        self.assertEqual(data.city_name, "Test City")
        self.assertEqual(data.weather_description, "clear sky")

    def test_print_weather_data(self):
        data_str = {"name": "Test City", "weather": [{"description": "clear sky"}],
                    "wind": {"speed": 5.5}, "main": {"temp": 293.15, "humidity": 50}}
        data = CityWeatherData.model_validate(data_str)
        self.assertEqual(str(data), "City: Test City\n"
                                    "    Temperature: 20.0 °C\n"
                                    "    Temperature: 68.0 °F\n"
                                    "    Humidity: 50 %\n"
                                    "    Wind Speed: 5.5 m/s\n"
                                    "    Weather Description: clear sky\n")

    def test_print_missing_fields(self):
        data_str = {"name": "Test City", "weather": [{"description": "clear sky"}]}
        data = CityWeatherData.model_validate(data_str)
        self.assertEqual(str(data), "City: Test City\n"
                                    "    Weather Description: clear sky\n")


if __name__ == "__main__":
    unittest.main()
