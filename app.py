from flask import Flask,request
from markupsafe import escape

app=Flask(__name__)
cities={"Riyadh":34,"Abha":13,"Jedda":40,"Dammam":41}

@app.route("/")
def getallciti():
    return cities

@app.route("/cities/<name>")
def one_city(name:str):
    return f"weather is{escape(cities[name])}"

@app.route("/city/all", methods=["GET"])
def displayPosts():
    if(request.args.get(sorted) is None):
        return f"{cities}"
    else:
        return "You need to provide query sort"