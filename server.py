from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city: str = request.args.get('city')

    if not bool(city.strip()):
        city = "Algiers"
        weather_data = get_current_weather(city)

    weather_data = get_current_weather(city)
    if weather_data['cod'] != 200:
        return render_template('city_not_found.html')

    return render_template('weather.html',  city=weather_data['name'].capitalize(), status=weather_data['weather'][0]['description'].capitalize(), temp=weather_data['main']['temp'], feels_like=weather_data['main']['feels_like'])


if __name__ == "__main__":
    app.config["DEBUG"] = True
    serve(app, host="localhost", port=5000)
