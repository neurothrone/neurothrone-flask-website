from flask import Blueprint

bp = Blueprint(name="book_library",
               import_name=__name__,
               template_folder="./templates",
               static_folder="static")

from app.blueprints.projects.cog.apps.book_library import routes
