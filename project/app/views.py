# views.py

from flask import render_template, request

from app import app

# Import all controllers
from app.controllers import *

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/insert')
def insert():
    return render_template("form.html")

# app.route('/hello')(hello.hi)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('form.html')
     
    if request.method == 'POST':
        try:
            return auth.login(request.form)
        except Exception as e:
            return(str(e))


