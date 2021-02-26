# web_routes.py

from flask import render_template

from app import app

# Define user routes
@app.route('/')
def index():
    return render_template("public/index.html")

@app.route('/about')
def about():
    return render_template("public/about.html")

@app.route('/blog')
def blog():
    return render_template("public/blog.html")

@app.route('/training')
def training():
    return render_template("public/training.html")

@app.route('/contact')
def contact():
    return render_template("public/contact.html")

# Define user routes
@app.route('/user/login')
def user_login():
    return render_template("user/login.html")

@app.route('/user/register')
def user_register():
    return render_template("user/register.html")

# Define admin routes
@app.route('/admin/login')
def admin_login():
    return render_template("admin/login.html")

@app.route('/admin/home')
def admin_home():
    return render_template("admin/home.html")

@app.route('/admin/blog')
def admin_blog():
    return render_template("admin/blog.html")