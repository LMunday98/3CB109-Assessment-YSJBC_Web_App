# app/__init__.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Setup SQL Alchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///desserts.db'
db = SQLAlchemy(app)

# Import web and api routes before running the app
# to prevent circular dependencies
from app.routes import *

# Load the config file
app.config.from_object('config')