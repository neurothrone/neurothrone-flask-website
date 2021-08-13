from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class: Config = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

from app import models
