import os
import requests

from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.blueprints.projects.jba.apps.weather_app import bp
from app.blueprints.projects.jba.apps.weather_app.model import City

UNITS = "metric"


@bp.route("/")
def index():
    cities = City.find_all()
    return render_template("weather_app/index.html",
                           title="Weather App",
                           weather=cities if cities else None)


@bp.route("/add", methods=["POST"])
def add_city():
    if request.method == "POST":
        # get name of city from POST request and capitalize the first letter of each word
        name = request.form["city_name"].title()

        if City.find_by_name(name):
            flash(f"The city '{name}' has already been added.", category="error")
        else:
            # get weather data for that city from open weather api
            api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}" \
                .format(name, os.environ["OPEN_WEATHER_KEY"], UNITS)

            # if a valid request
            if weather_data := requests.get(url=api_url):
                data_json = weather_data.json()

                # TODO: a list of images, check temperature, cold, warm, hot
                #       set appropriate image url

                # create an instance of CityModel and save to database
                city = City(name=name,
                            current_temp=int(data_json["main"]["temp"]),
                            current_state=data_json["weather"][0]["main"])
                city.save_to_db()
                flash(f"City '{city.name}' added.", category="success")
            else:
                flash(f"There is no city by that name.", category="error")

    return redirect(url_for("weather_app.index"))


@bp.route("/delete/<city_id>", methods=["GET", "POST"])
def delete_city(city_id: int):
    if city := City.find_by_id(city_id):
        city.delete_from_db()
        flash(f"City '{city.name}' deleted.", category="success")
    return redirect(url_for("weather_app.index"))
