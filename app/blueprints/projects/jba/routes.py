from app.blueprints.projects.jba import bp


@bp.route("/")
def test():
    return "JBA test"
