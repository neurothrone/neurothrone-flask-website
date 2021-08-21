from flask import Blueprint

bp = Blueprint(name="admin_book_library",
               import_name=__name__,
               template_folder="./templates",
               static_folder="static")

from app.blueprints.admin.apps.admin_book_library import routes
