from flask import Blueprint

bp = Blueprint(name="microblog",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.cog.apps.microblog import routes
