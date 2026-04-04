import datetime
from meteo import get_coordinates, get_forecast, formatPrint


if __name__ == "__main__":
    print("Python weather app")

    while True:
        user_input = input("\nEnter a location: (or type 'exit' to quit)\n").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        location = get_coordinates(user_input)

        if location:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            weather_data = get_forecast(
                location["lat"],
                location["lon"],
                location["altitude"],
                location["full_name"],
                now,
            )

            if weather_data:
                formatPrint(weather_data)
