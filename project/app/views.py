# views.py

from flask import render_template

from app import app

from app.controllers import *

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

app.route('/hello')(hello.hi)