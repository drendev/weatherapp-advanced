import datetime as dt
import requests

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius

def lookup(city):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "a4152a5b06c222cb1443badcf80e9052"

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city


    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_max = response['main']['temp_max']
    temp_min = response['main']['temp_min']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunrise = sunrise_time.strftime("%I : %M %P")
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    sunset = sunset_time.strftime("%I : %M %P")
    day_string = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    day = day_string.strftime("%A")
    date_string = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    date = date_string.strftime("%d %B %Y")
    return{
        "name": response['name'],
        "wed": response['weather'][0]['main'],
        "description": response['weather'][0]['description'],
        "humidity": response['main']['humidity'],
        "temp_celsius": kelvin_to_celsius_fahrenheit(temp_kelvin),
        "temp_max": round(float(kelvin_to_celsius_fahrenheit(temp_max)), 2),
        "temp_min": round(float(kelvin_to_celsius_fahrenheit(temp_min)), 2),
        "sunrise": sunrise,
        "sunset": sunset,
        "date": date,
        "day": day,
        "country": response['sys']['country'],
        "wind_speed": response['wind']['speed'],
        "long": response['coord']['lon'],
        "lat": response['coord']['lat'],
        }
