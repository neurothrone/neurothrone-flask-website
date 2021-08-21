from flask import render_template

from app.blueprints.projects.cog import bp


@bp.route("/")
def index():
    return render_template("cog/index.html",
                           title="Cortex of Growth Projects")
