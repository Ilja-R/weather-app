import unittest
from helper.weather_helper import get_celsius_from_kalvin, get_fahrenheit_from_kalvin


class TestWeatherHelper(unittest.TestCase):

    def test_celsius_conversion_is_correct_test(self):
        self.assertEqual(get_celsius_from_kalvin(273.15), 0.0)
        self.assertEqual(get_celsius_from_kalvin(0), -273.15)
        self.assertEqual(get_celsius_from_kalvin(300), 26.85)

    def test_fahrenheit_conversion_is_correct_test(self):
        self.assertEqual(get_fahrenheit_from_kalvin(273.15), 32.0)
        self.assertEqual(get_fahrenheit_from_kalvin(0), -459.67)
        self.assertEqual(get_fahrenheit_from_kalvin(300), 80.33)

    def test_celsius_conversion_with_negative_kelvin_test(self):
        self.assertRaises(ValueError, get_celsius_from_kalvin, -10)

    def test_fahrenheit_conversion_with_negative_kelvin_test(self):
        self.assertRaises(ValueError, get_fahrenheit_from_kalvin, -10)


if __name__ == "__main__":
    unittest.main()
