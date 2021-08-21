from flask import render_template

from app.blueprints.projects.cog.apps.microblog import bp


@bp.route("/")
def index():
    return render_template("microblog/index.html",
                           title="Microblog")
