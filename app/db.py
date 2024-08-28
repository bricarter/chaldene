from os import makedirs

from flask import current_app, g
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Base


engine = create_engine(f"sqlite+pysqlite:///{current_app.config['DATABASE']}", echo=False)


def connect_db():
    if 'db' not in g:
        g.db = Session(engine) 


def init_db():
    makedirs(current_app.instance_path, exist_ok=True)
    Base.metadata.create_all(engine)
    current_app.logger.info('database initialized')