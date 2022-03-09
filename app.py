from flask import Flask, request

app = Flask(__name__)

weather = {"makkah": 39, "riyadh": 40, "dammam": 43, "jeddah": 37,"abha": 26}


@app.route("/weather/<string:city>", methods = ["GET"])
def get_weather(city):
    order = request.args.get("order")
    # Dictionary will be returned sorted by default. Anyway, I wrote below code to sort 
    # the dictionary if requested
    if city == "all" and order == "sort":
        weather_sort = {}   
        for c in sorted(weather):
            weather_sort.update({c:weather[c]})
        return weather_sort
    elif city == "all" and order != "sort":
        return weather
    else:
        if city in weather:
            return str(weather[city])
        else:
            return f"Sorry, '{city}' is not exist"
        
