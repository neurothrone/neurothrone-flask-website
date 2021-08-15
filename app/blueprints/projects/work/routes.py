from flask import render_template

from app.blueprints.projects.work import bp


@bp.route("/")
def index():
    return render_template("work/index.html", title="Work")
