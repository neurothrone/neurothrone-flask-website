from flask import Blueprint

bp = Blueprint(name="jba",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.jba import routes
