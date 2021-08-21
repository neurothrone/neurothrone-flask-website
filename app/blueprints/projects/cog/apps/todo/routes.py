from flask import render_template

from app.blueprints.projects.cog.apps.todo import bp


@bp.route("/")
def index():
    return render_template("todo/index.html",
                           title="Todo")
