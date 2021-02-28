# api_routes.py

from flask import render_template, request

from models import *
from app import app

# Import all controllers
from app.controllers import *

# Define user api calls
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
     
    if request.method == 'POST':
        try:
            return auth.login(request.form)
        except Exception as e:
            return(str(e))

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
     
    if request.method == 'POST':
        try:
            return auth.register(request.form)
        except Exception as e:
            return(str(e))

@app.route('/logout')
def logout():
    try:
        return auth.logout()
    except Exception as e:
        return(str(e))

# Define admin api calls
@app.route('/admin/home')
def admin_home():
    try:
        users = User.query.all()
        return render_template('admin/home.html', users=users)
    except Exception as e:
        return(str(e))