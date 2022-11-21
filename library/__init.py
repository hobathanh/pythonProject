from flask import Flask, request, Blueprint
from .Products.controller import products
from .extension import db,ma
from .model import *
import os

def create_db(app):
    if not os.path.exists("library/library.db"):
        db.create_all(app=app)
        print("Created Success DB!")

def create_app(config_file="config.py"):
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_pyfile(config_file)
    create_db(app)
    app.register_blueprint(products)
    print(app.config["SECRET_KEY"])
    return app