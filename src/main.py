import datetime
from meteo import get_forecast


if __name__ == "__main__":

    print("Python weather app")
    # location = input("Enter a location: \n")
    
    lat = 47.07
    lon = 15.44
    name = "Graz"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    weather = get_forecast(lat, lon, name, now)

    print(weather)
