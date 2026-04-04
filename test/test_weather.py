import datetime
from src.meteo import get_forecast


def test_openmeteo():
    lat = 47.07
    lon = 15.44
    altitude = "666"
    name = "Graz"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert get_forecast(lat, lon, altitude, name, now)
