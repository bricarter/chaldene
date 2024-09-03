import os


basedir = os.path.abspath(os.path.dirname(__file__))

class TestingConfig:
    DATABASE = os.path.join(basedir, "tests/app.db")


class DevelopmentConfig:
    DATABASE = os.path.join(basedir, "instance/app.db")


class ProductionConfig:
    DATABASE = os.path.join(basedir, "instance/app.db")


config = {
        "testing": TestingConfig,
        "development": DevelopmentConfig,
        "production": ProductionConfig
        }