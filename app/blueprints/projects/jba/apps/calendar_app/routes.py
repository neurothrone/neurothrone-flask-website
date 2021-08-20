from flask import render_template

from app.blueprints.projects.jba.apps.calendar_app import bp


@bp.route("/")
def index():
    return render_template("calendar_app/index.html")
