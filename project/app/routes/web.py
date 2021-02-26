# web_routes.py

from flask import render_template

from app import app

# Define user routes
@app.route('/')
def index():
    return render_template("user/index.html")

@app.route('/about')
def about():
    return render_template("user/about.html")

@app.route('/blog')
def blog():
    return render_template("user/blog.html")

@app.route('/training')
def training():
    return render_template("user/training.html")

@app.route('/contact')
def contact():
    return render_template("user/contact.html")

# Define admin routes
@app.route('/admin/login')
def admin_login():
    return render_template("admin/index.html")

@app.route('/admin/register')
def admin_register():
    return render_template("admin/register.html")