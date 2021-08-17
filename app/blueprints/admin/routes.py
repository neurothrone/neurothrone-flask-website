from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from app.blueprints.admin import bp
from app.blueprints.admin.forms import AddBookForm
from app.models.book import BookModel


@bp.route("/")
def admin():
    return render_template("admin/admin.html", title="Admin")


@bp.route("/book-library", methods=["GET", "POST"])
def book_library():
    form = AddBookForm()
    if form.validate_on_submit():
        book = BookModel(name=form.name.data,
                         author=form.author.data,
                         category=form.category.data,
                         book_link=form.book_link.data,
                         image_link=form.image_link.data)
        book.save_to_db()
        flash(message=f"Book '{book.name}' added.", category="success")
        return redirect(url_for("admin.book_library"))
    return render_template("admin/book-library/books.html",
                           form=form,
                           title="Book Library")
