from flask import render_template

from app.blueprints.admin import bp


@bp.route("/")
def admin():
    return render_template("admin/admin.html")


@bp.route("/book-library")
def book_library():
    return render_template("admin/book-library.html")
