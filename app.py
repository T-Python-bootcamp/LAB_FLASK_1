from flask import Flask

app = Flask(__name__)

citys={"rafha":"rainy", "arar":"rainy","Hail":"sunny" ,"riyadh":"dust","madena":"cloudy"}


@app.route('/')
def all_citys():
    return citys 


@app.route("/weather/<city>")
def one_citys(city :str):
    if city in citys:
        return f"weather in   {city}"
    else:
        return("This city does not exist")   




@app.route("/city/sorted", methods=["GET"])
def viewAll_sorted():
     sort= list(citys.items())
     sort.sort(reverse=False)


     return f"{ sort}"    