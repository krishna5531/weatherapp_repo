from flask import  Flask , request, render_template
import requests
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route("/weatherapp", methods=['POST', "GET"])
def get_weather_data():
    url="https://api.weatherapi.com/v1/current.json"

    p={'key': request.form.get("apiid"),   #here request method/class of flask module is used 
        'q': request.form.get("city")
        }
    response = requests.get(url, params=p)   # here requests module is used 
    data = response.json()
    return f"data: {data}"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5002")
