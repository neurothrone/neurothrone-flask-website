from flask import Blueprint

bp = Blueprint(name="weather_app",
               import_name=__name__,
               template_folder="./templates",
               static_folder="static")

from app.blueprints.projects.jba.apps.weather_app import routes
