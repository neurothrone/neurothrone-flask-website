from flask import Blueprint

bp = Blueprint(name="work",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.work import routes
