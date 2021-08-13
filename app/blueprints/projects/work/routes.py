from app.blueprints.projects.work import bp


@bp.route("/")
def test():
    return "Work test"
