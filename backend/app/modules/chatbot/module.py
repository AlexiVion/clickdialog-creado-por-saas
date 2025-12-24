from flask import Flask
from .routes import bp
from . import models  # noqa: F401

def register(app: Flask):
    app.register_blueprint(bp)
