from flask import Blueprint

bp = Blueprint(name="eternity_of_code",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.cog.apps.eternity_of_code import routes
