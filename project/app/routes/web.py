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

@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/training')
def training():
    return render_template("training.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")