# app/__init__.py

from flask import Flask, request
from flask_mysqldb import MySQL
from app.db import connection

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

# Initalise mysql
mysql = MySQL(app)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        try:
            
            name = request.form['name']
            password = request.form['password']

            cursor, conn = connection()
            cursor.execute("insert into users (user_name,user_password) values(%s,%s)", (name,password))
            conn.commit()
            cursor.close()

            return("okay")
        except Exception as e:
            return(str(e))



        