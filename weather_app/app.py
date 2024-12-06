import weather
import asyncio


async def main():
    while True:
        user_input = input("Enter key or 'q' to quit: ")

        if user_input.strip().lower() == "q":
            break
        else:
            print(f"Getting weather for {user_input}\n")
            cities = user_input.split(",")
            city_weather = await weather.get_weather_list(cities)
            pretty_print(city_weather)

    print("Goodbye!")


def pretty_print(weather_data: tuple):
    def print_weather_data(city_weather_data):
        print(f"    Temperature: {city_weather_data.get('temp', 'N/A')}°C")
        print(f"    Temperature: {city_weather_data.get('temp_fahrenheit', 'N/A')}°F")
        print(f"    Weather: {city_weather_data.get('description', 'N/A')}")
        print(f"    Humidity: {city_weather_data.get('humidity', 'N/A')}%")
        print(f"    Wind Speed: {city_weather_data.get('wind_speed', 'N/A')} m/s")

    def print_error_data(error_data):
        print(f"    Error: {error_data.get('error', 'Unknown error')}")
        if 'status_code' in error_data:
            print(f"    Status Code: {error_data['status_code']}")
            print(f"    Reason: {error_data.get('reason', 'No reason provided')}")

    for data in weather_data:
        print(f"City: {data['city']}")
        if 'error' in data:
            print_error_data(data)
        else:
            print_weather_data(data)
        print()


if __name__ == "__main__":
    asyncio.run(main())
