# web_routes.py

from flask import render_template

from app import app

# Define routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/insert')
def insert():
    return render_template("form.html")

@app.route('/form')
def form():
    return render_template('form.html')