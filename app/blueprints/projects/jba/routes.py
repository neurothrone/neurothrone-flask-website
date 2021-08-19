import os
import requests

from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from app.blueprints.projects.jba import bp
from app.models.jba.weather_app import CityModel

UNITS = "metric"


@bp.route("/")
def index():
    return render_template("jba/index.html",
                           title="JetBrains Academy Projects")


@bp.route("/calendar-app")
def calendar_app():
    return render_template("jba/calendar-app/main.html",
                           title="Calendar App")


@bp.route("/weather-app")
def weather_app():
    cities = CityModel.find_all()
    return render_template("jba/weather-app/main.html",
                           title="Weather App",
                           weather=cities if cities else None)


@bp.route("/weather-app/add", methods=["POST"])
def add_city():
    if request.method == "POST":
        # get name of city from POST request and capitalize the first letter of each word
        name = request.form["city_name"].title()

        if CityModel.find_by_name(name):
            flash("The city has already been added to the list!")
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
                city = CityModel(name=name,
                                 current_temp=int(data_json["main"]["temp"]),
                                 current_state=data_json["weather"][0]["main"])
                city.save_to_db()
            else:
                flash("The city doesn't exist!")

    return redirect(url_for("jba.weather_app"))


@bp.route("/weather-app/delete/<city_id>", methods=["GET", "POST"])
def delete_city(city_id: int):
    if city := CityModel.find_by_id(city_id):
        city.delete_from_db()
    return redirect(url_for("jba.weather_app"))
