from flask import render_template

from app.blueprints.projects.cog.apps.microblog import bp
from app.blueprints.projects.cog.apps.microblog.model import Micropost


@bp.route("/")
def index():
    return render_template("microblog/index.html",
                           microposts=Micropost.find_all(),
                           title="Microblog")
