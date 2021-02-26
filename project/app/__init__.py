# app/__init__.py

from flask import Flask, request

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import web_routes

# Load the api routes
from app import api_routes

# Load the config file
app.config.from_object('config')