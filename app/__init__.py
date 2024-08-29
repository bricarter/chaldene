import os
import logging

from flask import Flask

from config import config


def create_app(config_name="development"):
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename="logs/app_logs.log", level="INFO")

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    with app.app_context():
        from .db import init_db
        init_db()

        from . import api

    return app