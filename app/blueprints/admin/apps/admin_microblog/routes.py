from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from app.blueprints.admin.apps.admin_microblog import bp
from app.blueprints.admin.apps.admin_microblog.forms import AddPostForm
from app.blueprints.admin.apps.admin_microblog.forms import EditPostForm
from app.blueprints.projects.cog.apps.microblog.model import Micropost


@bp.route("/")
def index():
    return render_template("admin_microblog/index.html",
                           microposts=Micropost.find_all(),
                           title="Microblog")


@bp.route("/post/add", methods=["GET", "POST"])
def add_post():
    form = AddPostForm()
    if form.validate_on_submit():
        post = Micropost(title=form.title.data,
                         body=form.body.data)
        post.save_to_db()
        flash(message="Post added.", category="success")
        return redirect(url_for("admin_microblog.index"))
    return render_template("admin_microblog/post.html",
                           form=form,
                           form_type="ADD",
                           title="Microblog")


@bp.route("/post/edit/<post_id>", methods=["GET", "POST"])
def edit_post(post_id: int):
    post = Micropost.find_by_id(post_id)
    form = EditPostForm()

    if form.validate_on_submit():
        new_data = {
            "title": form.title.data,
            "body": form.body.data,
        }
        post.update(new_data)
        flash("Post updated.", category="success")
        return redirect(url_for("admin_microblog.index"))

    form.title.data = post.title
    form.body.data = post.body

    return render_template("admin_microblog/post.html",
                           post=post,
                           form=form,
                           form_type="EDIT",
                           title="Microblog")


@bp.route("/post/delete/<post_id>", methods=["POST"])
def delete_post(post_id: int):
    if post := Micropost.find_by_id(post_id):
        post.delete_from_db()
        flash("Post deleted.", category="success")
    return redirect(url_for("admin_microblog.index"))


@bp.route("/post/<post_id>", methods=["GET"])
def view_post(post_id: int):
    if post := Micropost.find_by_id(post_id):
        return render_template("admin_microblog/view_post.html",
                               title="Microblog",
                               post=post)
    return redirect(url_for("admin_microblog.index"))
