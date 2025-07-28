import asyncio
from weather import getWeather, format_and_print_weather


print("Python weather app")
location = input("Enter a location: \n")
weather_graz = asyncio.run(getWeather(location))
format_and_print_weather(weather_graz)
