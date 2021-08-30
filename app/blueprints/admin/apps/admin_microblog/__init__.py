from flask import Blueprint

bp = Blueprint(name="admin_microblog",
               import_name=__name__,
               static_folder="static",
               template_folder="./templates")

from app.blueprints.admin.apps.admin_microblog import routes
