from flask import Blueprint

bp = Blueprint(name="admin",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.admin import routes
