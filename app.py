from flask import Flask,request


app = Flask(__name__)

cities = {"Riyadh": 33, "Abha": 14, "Jeddah": 29, "Dammam": 30}


@app.route("/city", methods=["GET"])
def viewAll():
    return cities


@app.route("/city/<name>")
def viewOne(name: str):
    return f"the weather in {name} is {cities[name]}"


@app.route("/city/sorted", methods=["GET"])
def viewAll_sorted():
    sorted_cities = list(cities.items())
    sorted_cities.sort(reverse=False)
    
    
    return f"{dict(sorted_cities)}"

