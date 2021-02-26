# views.py

from flask import render_template, request
from flask_mysqldb import MySQL

from app import app

from app.controllers import *

@app.route('/')
def index():
    return render_template("form.html")


@app.route('/about')
def about():
    return render_template("about.html")

app.route('/hello')(hello.hi)

@app.route('/form')
def form():
    return render_template('form.html')

