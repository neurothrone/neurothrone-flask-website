from flask import render_template

from app.blueprints.projects.jba import bp


@bp.route("/")
def index():
    return render_template("jba/index.html", title="JetBrains Academy")
