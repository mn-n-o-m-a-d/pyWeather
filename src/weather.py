import python_weather
import sys


async def getWeather(locationName: str):
    try:
        async with python_weather.Client(unit=python_weather.METRIC) as client:
            weather = await client.get(locationName)

            current_data = {
                "location": weather.location,
                "temperature": weather.temperature,
                "description": weather.description,
                "feels_like": weather.feels_like,
                "humidity": weather.humidity,
                "pressure": weather.pressure,
                "wind_speed": weather.wind_speed,
                "forecast_unit": "C",
            }

            daily_forecasts = []
            for daily_data in weather.daily_forecasts:
                hourly_forecasts = []
                for hourly_data in daily_data.hourly_forecasts:
                    hourly_forecasts.append(
                        {
                            "time": hourly_data.time.strftime("%H:%M"),
                            "temperature": hourly_data.temperature,
                            "description": hourly_data.description,
                        }
                    )
                daily_forecasts.append(
                    {
                        "date": daily_data.date.strftime("%Y-%m-%d"),
                        "temperature": daily_data.temperature,
                        "description": daily_data.date,
                        "lowest_temperature": daily_data.lowest_temperature,
                        "highest_temperature": daily_data.highest_temperature,
                        "hourly": hourly_forecasts,
                    }
                )

            return {"current": current_data, "dailyForecasts": daily_forecasts}

    except python_weather.exceptions.OpenWeatherMapError as e:
        return {"error": f"Weather-Service error: {e}"}
    except Exception as e:
        return {"error": f"Unkown error: {e}"}


def format_and_print_weather(weather_data: dict):
    if "error" in weather_data:
        print(f"\nFEHLER: {weather_data['error']}", file=sys.stderr)
        return

    current = weather_data.get("current")
    daily_forecasts = weather_data.get("dailyForecasts")
    unit = current.get("forecast_unit", "°")

    print("\n" + "=" * 40)
    print(f"Current weather for {current['location']}")
    print("=" * 40)
    print(f" Temperature: {current['temperature']}{unit}")
    print(f" Feels like: {current['feels_like']}{unit}")
    print(f" Description: {current['description']}")
    print(f" Humidity: {current['humidity']}%")
    print(f" Wind speed: {current['wind_speed']} m/s")
    print(f" Air pressure: {current['pressure']} hPa")

    print("\n" + "-" * 40)
    print("Daily forecast:")
    print("-" * 40)
    for daily in daily_forecasts:
        print(f"Date: {daily['date']}")
        print(f"  Daytime temperature: {daily['temperature']}{unit}")
        print(
            f"  Minimum/highest temperature: {daily['lowest_temperature']}{unit} / {daily['highest_temperature']}{unit}"
        )
        print(f"  Description: {daily['description']}")
        if daily["hourly"]:
            print("  Hourly forecast:")
            for hourly in daily["hourly"]:
                print(
                    f"    {hourly['time']}: {hourly['temperature']}{unit} - {hourly['description']}"
                )
        else:
            print("  No hourly forecast available.")
    print("\n" + "=" * 40 + "\n")