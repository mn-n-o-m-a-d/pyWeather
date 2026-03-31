import requests


def get_coordinates(cityname):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={cityname}&count=1&language=de&format=json"

    try:
        response = requests.get(geo_url)
        response.raise_for_status()
        data = response.json()

        if "results" in data:
            result = data["results"][0]
            return {
                "lat": result["latitude"],
                "lon": result["longitude"],
                "full_name": f"{result['name']} ({result.get('admin1', 'Unbekannt')}, {result.get('country', '')})"
            }
        else:
            print(f"Location '{cityname}' not found.")
            return None
    except Exception as e:
        print(f"Error to find location: {e}")
        return None


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


def formatPrint(data):
    if not data:
        return
    
    weather_icons = {
        # Sonnig & Klar
        0:  "☀️",  # Klarer Himmel
        1:  "🌤️",  # Hauptsächlich klar
        2:  "⛅",  # Teilweise bewölkt
        3:  "☁️",  # Bedeckt

        # Nebel
        45: "🌫️",  # Nebel
        48: "🌫️",  # Reifnebel

        # Nieselregen (Drizzle)
        51: "🌦️",  # Leichter Nieselregen
        53: "🌦️",  # Mäßiger Nieselregen
        55: "🌧️",  # Dichter Nieselregen
        56: "🌨️",  # Gefrierender Nieselregen: Leicht
        57: "🌨️",  # Gefrierender Nieselregen: Dicht

        # Regen
        61: "🌧️",  # Leichter Regen
        63: "🌧️",  # Mäßiger Regen
        65: "🌧️",  # Starker Regen
        66: "🧊",  # Gefrierender Regen: Leicht
        67: "🧊",  # Gefrierender Regen: Stark

        # Schnee & Graupel
        71: "❄️",  # Leichter Schneefall
        73: "❄️",  # Mäßiger Schneefall
        75: "❄️",  # Starker Schneefall
        77: "🌨️",  # Schneegriesel (Hagel/Graupel)

        # Schauer
        80: "🌦️",  # Leichte Regenschauer
        81: "🌦️",  # Mäßige Regenschauer
        82: "🌧️",  # Starke Regenschauer
        85: "🌨️",  # Leichte Schneeschauer
        86: "❄️",  # Starke Schneeschauer

        # Gewitter
        95: "⛈️",  # Gewitter: Leicht oder mäßig
        96: "🌩️",  # Gewitter mit leichtem Hagel
        99: "⚡",  # Gewitter mit starkem Hagel
    }

    print(f"\n>>> Weather for {data['name']} <<<")
    print(f"Timestamp: {data['timestamp']}")
    print(f"{'Datum':<12} | {'Max':<7} | {'Min':<7} | {'Code'}")
    print("-" * 40)
    for day in data["forecast"]:
        icon = weather_icons.get(day['code'], "❓")
        print(
            f"{day['date']:<12} | {day['temp_max']:>5}°C | {day['temp_min']:>5}°C | {icon}"
        )
