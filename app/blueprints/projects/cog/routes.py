from flask import render_template

from app.blueprints.projects.cog import bp
from app.models.book import BookModel


@bp.route("/")
def test():
    return "Cog test"


@bp.route("/book-library")
def book_library():
    books = BookModel.find_all()
    return render_template("cog/book-library.html",
                           books=books,
                           title="Book Library")
