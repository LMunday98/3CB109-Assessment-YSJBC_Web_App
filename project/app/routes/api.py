# api_routes.py

from flask import render_template, request

from app import app

# Import all controllers
from app.controllers import *

# Define api calls
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        try:
            return auth.login(request.form)
        except Exception as e:
            return(str(e))

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        try:
            return auth.register(request.form)
        except Exception as e:
            return(str(e))


