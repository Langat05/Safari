from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap


# Initializing application

app = Flask(__name__)
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app)

from app import views
from app import error