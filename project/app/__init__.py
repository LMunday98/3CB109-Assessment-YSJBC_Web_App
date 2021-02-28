# app/__init__.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Setup SQL Alchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///desserts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@127.0.0.1/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Load the config file
app.config.from_object('config')

db = SQLAlchemy(app)
