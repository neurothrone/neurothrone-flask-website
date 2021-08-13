from flask import render_template

from app.blueprints.admin import bp


@bp.route("/", subdomain="admin")
def admin():
    return render_template("admin/admin.html")


@bp.route("/book-library", subdomain="admin")
def book_library():
    return render_template("admin/book-library.html")
