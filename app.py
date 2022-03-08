from flask import Flask, request
from collections import OrderedDict

app = Flask(__name__)

citiyes = {"Riyadh" : 24 , "Abha" : 12, "Jedda" : 28, "Dammam" :29}

@app.route("/cities/all")
def allCities():
    return citiyes

@app.route("/cities/<city>")
def get_city(city : str):
    return f"The weather for {city} is {citiyes[city]}"






# @app.route("/cities/sort" ,  methods = ["GET"])
# def cities_sorted():
#     global citiyes
#     isSorted =  request.args.get(citiyes.key , default=True)
#     if isSorted is None:
#         return "You list sorted {citiyes}"
#     else : 
#         "None sorted"