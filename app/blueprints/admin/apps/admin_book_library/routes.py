from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from app.blueprints.admin.apps.admin_book_library import bp
from app.blueprints.admin.apps.admin_book_library.forms import AddBookForm
from app.blueprints.admin.apps.admin_book_library.forms import EditBookForm
from app.blueprints.projects.cog.apps.book_library.model import Book


@bp.route("/", methods=["GET", "POST"])
def index():
    books = Book.find_all()
    return render_template("admin_book_library/index.html",
                           books=books,
                           title="Admin Book Library")


@bp.route("/book/add", methods=["GET", "POST"])
def add_book():
    form = AddBookForm()
    if form.validate_on_submit():
        book = Book(name=form.name.data,
                    author=form.author.data,
                    category=form.category.data,
                    book_link=form.book_link.data,
                    image_link=form.image_link.data)
        book.save_to_db()
        flash(message=f"Book '{book.name}' added.", category="success")
        return redirect(url_for("admin_book_library.index"))
    return render_template("admin_book_library/book.html",
                           form=form,
                           form_type="ADD",
                           title="Admin Book Library")


@bp.route("/book/edit/<book_id>", methods=["GET", "POST"])
def edit_book(book_id: int):
    book = Book.find_by_id(book_id)
    form = EditBookForm()

    if form.validate_on_submit():
        new_data = {
            "name": form.name.data,
            "author": form.author.data,
            "category": form.category.data,
            "book_link": form.book_link.data,
            "image_link": form.image_link.data
        }
        book.update(new_data)
        flash(f"Book '{book.name}' updated.", category="success")
        return redirect(url_for("admin_book_library.index"))

    form.name.data = book.name
    form.author.data = book.author
    form.category.data = book.category
    form.book_link.data = book.book_link
    form.image_link.data = book.image_link

    return render_template("admin_book_library/book.html",
                           book=book,
                           form=form,
                           form_type="EDIT",
                           title="Admin Book Library")


@bp.route("/book/delete/<book_id>", methods=["POST"])
def delete_book(book_id: int):
    if book := Book.find_by_id(book_id):
        book.delete_from_db()
        flash(f"Book '{book.name}' deleted.", category="success")
    return redirect(url_for("admin_book_library.index"))


@bp.route("/book/<book_id>", methods=["GET"])
def view_book(book_id: int):
    if book := Book.find_by_id(book_id):
        print(book)
        return render_template("admin_book_library/view_book.html",
                               title="Admin Book Library",
                               book=book)
    return redirect(url_for("admin_book_library.index"))
