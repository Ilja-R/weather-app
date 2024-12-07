from service import weather
import asyncio
from collections import OrderedDict


async def main():
    while True:
        user_input = input("Enter cities seperated by comma and hit enter or use 'q' to quit: ")

        if user_input.strip().lower() == "q":
            break
        else:
            cities = list(OrderedDict.fromkeys(city.strip().lower() for city in user_input.split(",") if city.strip()))
            print(f"Fetching weather data for {', '.join(cities)}\n")
            weather_fetch_results = await weather.get_weather_from_list(cities)
            for data in weather_fetch_results:
                print(str(data))

    print("Goodbye!")


if __name__ == "__main__":
    asyncio.run(main())
