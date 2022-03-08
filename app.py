from typing import OrderedDict
from flask import Flask, jsonify, request

app = Flask(__name__)

cities = {
     "riyadh": "sunny",  
     "abha": "rain",
     "jeddah": "sunny",
     "dammam": "cloudy",
}

@app.route("/weather/all", methods=["GET"])
def get_all():
    return cities

@app.route("/weather/<city>", methods=["GET"])
def get_weather(city: str):
    if city in cities:
        return cities[city]
    else:
        return "city is not covered"

@app.route("/weather")
def sorted_cities():
    isSorted = request.args.get("sorted", default=False)
    if isSorted:
        return OrderedDict(cities)
    else:
        return cities
    