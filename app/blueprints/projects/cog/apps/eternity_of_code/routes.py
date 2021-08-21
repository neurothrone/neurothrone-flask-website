from flask import render_template

from app.blueprints.projects.cog.apps.eternity_of_code import bp


@bp.route("/")
def index():
    return render_template("eternity_of_code/index.html",
                           title="Eternity of Code")
