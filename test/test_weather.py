from src.weather import getWeather


def test_get_weather():
    assert getWeather("Graz")
    