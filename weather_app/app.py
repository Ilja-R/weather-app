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
    for data in weather_data:
        print(f"City: {data['key']}")

        if 'error' in data:
            print(f"    Error: {data['error']}")
            print()
        else:
            print(f"    Temperature: {data['temp']}°C")
            print(f"    Temperature: {data['temp_fahrenheit']}°F")
            print(f"    Weather: {data['description']}")
            print(f"    Humidity: {data['humidity']}%")
            print(f"    Wind Speed: {data['wind_speed']}m/s")
            print()


if __name__ == "__main__":
    asyncio.run(main())
