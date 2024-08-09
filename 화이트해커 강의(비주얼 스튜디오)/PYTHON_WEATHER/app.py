from flask import Flask, render_template, request
import requests
app = Flask(__name__)

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        city = request.form["city"]
        api_key = "daacd8a9f729a351f1dbe6d1e93d00f3"
        weather_data = get_weather(city, api_key)
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        return render_template("result.html", city=city, temp=temp, feels_like=feels_like)
    
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)