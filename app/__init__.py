from typing import Type

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from config import Config

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
    app.register_blueprint(admin_bp, subdomain="admin")

    # main section
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    # project section
    # cog section
    from app.blueprints.projects.cog import bp as cog_bp
    app.register_blueprint(cog_bp, subdomain="projects", url_prefix="/cog")

    # jba section
    from app.blueprints.projects.jba import bp as jba_bp
    app.register_blueprint(jba_bp, subdomain="projects", url_prefix="/jba")

    # calendar app
    from app.blueprints.projects.jba.apps.calendar_app import bp as calendar_app_bp
    from app.blueprints.projects.jba.apps.calendar_app.api import init_api_routes as init_calendar_api
    api.init_app(calendar_app_bp)
    init_calendar_api(api)
    app.register_blueprint(calendar_app_bp, subdomain="api", url_prefix="/jba/calendar")

    # weather app
    from app.blueprints.projects.jba.apps.weather_app import bp as weather_app_bp
    app.register_blueprint(weather_app_bp, subdomain="projects", url_prefix="/jba/weather-app")

    # work section
    from app.blueprints.projects.work import bp as work_bp
    app.register_blueprint(work_bp, subdomain="projects", url_prefix="/work")

    return app

from app import models
