# app/__init__.py

from flask import Flask, request

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Import web and api routes
from app.routes import *

# Load the config file
app.config.from_object('config')