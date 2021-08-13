from flask import render_template

from app.blueprints.projects.cog import bp


@bp.route("/")
def test():
    return "Cog test"


@bp.route("/book-library")
def book_library():
    return render_template("cog/book-library.html")
