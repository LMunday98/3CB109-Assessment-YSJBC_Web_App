# app/__init__.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Setup SQL Alchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@127.0.0.1/flask'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://luke.munday:xPH89C6z9OrABOO2@127.0.0.1/luke.munday'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Load the config file
app.config.from_object('config')

# Define app wide db instance
db = SQLAlchemy(app)

# Define bcrypt
bcrypt = Bcrypt(app)