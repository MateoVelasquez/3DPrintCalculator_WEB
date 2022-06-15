import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import set_environtment_config

set_environtment_config()
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    environment_cfg = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_cfg)
    db.init_app(app)

    with app.app_context():
        from .routers import calculator_api
        app.register_blueprint(calculator_api)
        return app