from flask import Blueprint

bp = Blueprint(name="book_library",
               import_name=__name__,
               template_folder="./templates")

from app.blueprints.projects.cog.apps.book_library import routes
