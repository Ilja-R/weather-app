import unittest


class TestWeatherFetchException(unittest.TestCase):

    def test_weather_print_method_all_fields(self):
        from src.exception.weather_exception import WeatherFetchException
        exception = WeatherFetchException("Test Message", "Test City", 404, "Not Found")
        expected_str = (
            "City: Test City\n"
            "    Error: Test Message\n"
            "    Status code: 404\n"
            "    Reason: Not Found\n"
        )
        self.assertEqual(str(exception), expected_str)

    def test_weather_print_method_missing_fields(self):
        from src.exception.weather_exception import WeatherFetchException
        exception = WeatherFetchException("Test Message", "Test City")
        expected_str = (
            "City: Test City\n"
            "    Error: Test Message\n"
        )
        self.assertEqual(str(exception), expected_str)


if __name__ == "__main__":
    unittest.main()
