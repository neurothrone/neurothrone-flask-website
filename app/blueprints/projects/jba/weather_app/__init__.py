from flask import Blueprint

bp = Blueprint(name="weather_app",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.jba.weather_app import routes
