
def get_celsius_from_kalvin(temp_kelvin: float) -> float:
    if temp_kelvin < 0:
        raise ValueError("Temperature cannot be negative.")
    return round(temp_kelvin - 273.15, 2)


def get_fahrenheit_from_kalvin(temp_kelvin: float) -> float:
    if temp_kelvin < 0:
        raise ValueError("Temperature cannot be negative.")
    return round((temp_kelvin - 273.15) * 9 / 5 + 32, 2)