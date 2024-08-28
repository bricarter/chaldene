import os
import logging

from flask import Flask


def create_app():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename="logs/app_logs.log", level="INFO")

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello, World."

    return app