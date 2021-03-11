import os
from flask_sqlalchemy import SQLAlchemy

os_database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()


def setup_db(app, database_path=os_database_path):
    """ setup_db(app) binds a flask application and a SQLAlchemy service """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
