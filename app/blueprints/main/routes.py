from flask import render_template

from app.blueprints.main import bp


@bp.route("/")
def index():
    return render_template("main/index.html", title="Home")


@bp.route("/about")
def about():
    return render_template("main/about.html", title="About")


@bp.route("/projects")
def projects():
    return render_template("main/projects.html", title="Projects")


@bp.route("/contact")
def contact():
    return render_template("main/contact.html", title="Contact")
