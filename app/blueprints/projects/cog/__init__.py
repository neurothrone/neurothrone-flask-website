from flask import Blueprint

bp = Blueprint(name="cog",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.cog import routes
