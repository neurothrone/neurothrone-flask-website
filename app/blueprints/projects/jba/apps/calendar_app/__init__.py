from flask import Blueprint

bp = Blueprint(name="calendar_app",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.jba.apps.calendar_app import routes
