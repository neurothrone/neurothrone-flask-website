from flask import render_template

from app.blueprints.projects.cog.apps.book_library import bp
from app.blueprints.projects.cog.apps.book_library.model import BookCategory
from app.blueprints.projects.cog.apps.book_library.model import Book


@bp.route("/")
def index():
    return render_template("book_library/index.html",
                           books=Book.find_all(),
                           title="Book Library",
                           category=BookCategory)


# @bp.route("/book-library/book", methods=["POST"])
# def create_book():
#     from src.models.book import BookModel
#     args = request.form
#     book = BookModel(**args)
#     book.save_to_db()
#     return redirect("/admin/book-library")
