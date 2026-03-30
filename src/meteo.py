import requests


def get_forecast(lat, lon, name, timestamp):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=weather_code,temperature_2m_max,temperature_2m_min&timezone=Europe%2FBerlin"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        daily_data = data["daily"]
        forecast_days = []

        for i in range(len(daily_data["time"])):
            forecast_days.append(
                {
                    "date": daily_data["time"][i],
                    "code": daily_data["weather_code"][i],
                    "temp_max": daily_data["temperature_2m_max"][i],
                    "temp_min": daily_data["temperature_2m_min"][i],
                }
            )

        return {"name": name, "timestamp": timestamp, "forecast": forecast_days}
    except Exception as e:
        print(f"Error at {name}: {e}")
        return None
