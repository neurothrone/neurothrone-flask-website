from flask import render_template

from app.blueprints.projects.cog import bp
from app.models.book import BookModel
from app.models.book import BookCategory


@bp.route("/")
def index():
    return render_template("cog/index.html",
                           title="Cortex of Growth")


@bp.route("/book-library")
def book_library():
    return render_template("cog/book-library/main.html",
                           books=BookModel.find_all(),
                           title="Book Library",
                           category=BookCategory)


@bp.route("/eternity-of-code")
def eternity_of_code():
    return render_template("cog/eternity-of-code/main.html",
                           title="Eternity of Code")


@bp.route("/microblog")
def microblog():
    return render_template("cog/microblog/main.html",
                           title="Microblog")


@bp.route("/todo")
def todo():
    return render_template("cog/todo/main.html",
                           title="Todo")


# @bp.route("/book-library/book", methods=["POST"])
# def create_book():
#     from src.models.book import BookModel
#     args = request.form
#     book = BookModel(**args)
#     book.save_to_db()
#     return redirect("/admin/book-library")
