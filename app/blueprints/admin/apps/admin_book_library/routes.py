from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from app.blueprints.admin.apps.admin_book_library import bp
from app.blueprints.admin.apps.admin_book_library.forms import AddBookForm
from app.blueprints.projects.cog.apps.book_library.model import Book


@bp.route("/", methods=["GET", "POST"])
def index():
    form = AddBookForm()
    if form.validate_on_submit():
        book = Book(name=form.name.data,
                    author=form.author.data,
                    category=form.category.data,
                    book_link=form.book_link.data,
                    image_link=form.image_link.data)
        book.save_to_db()
        flash(message=f"Book '{book.name}' added.", category="success")
        return redirect(url_for("admin.book_library"))
    return render_template("admin_book_library/index.html",
                           form=form,
                           title="Admin Book Library")
