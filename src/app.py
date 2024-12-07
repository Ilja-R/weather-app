from service import weather
import asyncio


async def main():
    while True:
        user_input = input("Enter cities seperated by comma and hit enter or use 'q' to quit: ")

        if user_input.strip().lower() == "q":
            break
        else:
            print(f"Getting weather for {user_input}\n")
            cities = user_input.split(",")
            city_weather = await weather.get_weather_from_list(cities)
            for data in city_weather:
                print(data)

    print("Goodbye!")


if __name__ == "__main__":
    asyncio.run(main())
