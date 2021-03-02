# api_routes.py

from flask import render_template, request, redirect

from models import *
from app import app

# Import all controllers
from app.controllers import *

# Define auth api calls
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
     
    if request.method == 'POST':
        try:
            return auth_controller.login(request.form)
        except Exception as e:
            return(str(e))

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('auth/register.html')
     
    if request.method == 'POST':
        try:
            return auth_controller.register(request.form)
        except Exception as e:
            return(str(e))

@app.route('/logout')
def logout():
    try:
        return auth_controller.logout()
    except Exception as e:
        return(str(e))

# Define blog api calls
@app.route('/blog/update', methods = ['POST', 'GET'])
def blog_update():
    if request.method == 'GET':
        return redirect('/admin/blog')
     
    if request.method == 'POST':
        try:
            return blog_controller.update(request.form)
        except Exception as e:
            return(str(e))