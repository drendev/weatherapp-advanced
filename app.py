from cs50 import SQL
from flask import Flask, render_template, request, redirect

from weather import lookup

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    "main page, default will be the location of the user"
    if request.method == "POST":
        search = request.form.get("search_city")
        lookedUp = lookup(search)
        if search == None:
            return redirect("/")
        else:
            name = lookedUp["name"]
            description = lookedUp["description"]
            humidity = lookedUp["humidity"]
            temp = round(float(lookedUp["temp_celsius"]), 2)
            sunrise = lookedUp["sunrise"]
            sunset = lookedUp["sunset"]
            country = lookedUp["country"]
            windspeed = lookedUp["wind_speed"]
            long = lookedUp["long"]
            lat = lookedUp["lat"]
            date = lookedUp["date"]
            day = lookedUp["day"]
            tempmax = lookedUp["temp_max"]
            tempmin = lookedUp["temp_min"]
            weather = lookedUp["wed"]

            return render_template("weather.html", name=name, description=description, humidity=humidity, temp=temp, sunrise=sunrise, sunset=sunset, country=country, windspeed=windspeed, long=long, lat=lat, day=day, date=date, tempmax=tempmax, tempmin=tempmin, weather=weather)
    else:
        return render_template("index.html")
@app.route('/weather', methods=["GET", "POST"])
def weather():
    if request.method == "POST":
        search = request.form.get("search_city")
        lookedUp = lookup(search)
        if lookedUp == None:
            print("Error")
        else:
            name = lookedUp["name"]
            description = lookedUp["description"]
            humidity = lookedUp["humidity"]
            temp = round(float(lookedUp["temp_celsius"]), 2)
            sunrise = lookedUp["sunrise"]
            sunset = lookedUp["sunset"]
            country = lookedUp["country"]
            windspeed = lookedUp["wind_speed"]
            long = lookedUp["long"]
            lat = lookedUp["lat"]
            date = lookedUp["date"]
            day = lookedUp["day"]
            tempmax = lookedUp["temp_max"]
            tempmin = lookedUp["temp_min"]
            return render_template("weather.html", name=name, description=description, humidity=humidity, temp=temp, sunrise=sunrise, sunset=sunset, country=country, windspeed=windspeed, long=long, lat=lat, day=day, date=date, tempmax=tempmax, tempmin=tempmin)
    else:
        return render_template("index.html")
