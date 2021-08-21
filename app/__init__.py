from datetime import date
from typing import Type

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config


class Subdomain:
    ADMIN = "admin"
    API = "api"
    BLOG = "blog"
    PROJECTS = "projects"


api = Api()
cors = CORS()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config: Type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    # admin section
    from app.blueprints.admin import bp as admin_bp
    app.register_blueprint(blueprint=admin_bp,
                           subdomain=Subdomain.ADMIN)

    from app.blueprints.admin.apps.admin_book_library import bp as admin_book_library_bp
    app.register_blueprint(blueprint=admin_book_library_bp,
                           subdomain=Subdomain.ADMIN,
                           url_prefix="/book-library")

    # main section
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(blueprint=main_bp)

    # project section
    # cog section
    from app.blueprints.projects.cog import bp as cog_bp
    app.register_blueprint(blueprint=cog_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/cog")

    from app.blueprints.projects.cog.apps.book_library import bp as book_library_bp
    app.register_blueprint(blueprint=book_library_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/cog/book-library")

    from app.blueprints.projects.cog.apps.eternity_of_code import bp as eternity_bp
    app.register_blueprint(blueprint=eternity_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/cog/eternity-of-code")

    from app.blueprints.projects.cog.apps.microblog import bp as microblog_bp
    app.register_blueprint(blueprint=microblog_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/cog/microblog")

    from app.blueprints.projects.cog.apps.todo import bp as todo_bp
    app.register_blueprint(blueprint=todo_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/cog/todo")

    # jba section
    from app.blueprints.projects.jba import bp as jba_bp
    app.register_blueprint(blueprint=jba_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/jba")

    # calendar app
    from app.blueprints.projects.jba.apps.calendar_app import bp as calendar_app_bp
    from app.blueprints.projects.jba.apps.calendar_app.api import init_api_routes as init_calendar_api
    api.init_app(calendar_app_bp)
    init_calendar_api(api)
    app.register_blueprint(blueprint=calendar_app_bp,
                           subdomain=Subdomain.API,
                           url_prefix="/jba/calendar")

    # weather app
    from app.blueprints.projects.jba.apps.weather_app import bp as weather_app_bp
    app.register_blueprint(blueprint=weather_app_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/jba/weather-app")

    # work section
    from app.blueprints.projects.work import bp as work_bp
    app.register_blueprint(blueprint=work_bp,
                           subdomain=Subdomain.PROJECTS,
                           url_prefix="/work")

    @app.context_processor
    def inject_current_year():
        return dict(current_year=date.today().year)

    return app


from app import models
