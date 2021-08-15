from flask import render_template

from app.blueprints.projects.cog import bp
from app.models.book import BookModel
from app.models.book import BookCategory


@bp.route("/")
def test():
    return "Cog test"


@bp.route("/book-library")
def book_library():
    books = BookModel.find_all()
    return render_template("cog/book-library/books.html",
                           books=books,
                           title="Book Library",
                           category=BookCategory)
