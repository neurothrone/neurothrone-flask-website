from flask import Blueprint

bp = Blueprint(name="todo",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.cog.apps.todo import routes
