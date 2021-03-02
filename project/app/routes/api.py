# api_routes.py

from flask import render_template, request, redirect

from models import *
from app import app

# Import all controllers
from app.controllers import *

# Define public api calls
@app.route('/blog')
def blog_view_all(id=None):
    return blog_controller.get(id, "public")

@app.route('/blog/<id>')
def blog_view_one(id=None):
    return blog_controller.get(id, "public", "ViewOne")

# Define auth api calls
@app.route('/login', methods = ['POST', 'GET'])
def login():
    return auth_controller.login(request.method, request.form)
        
@app.route('/register', methods = ['POST', 'GET'])
def register():
    return auth_controller.register(request.form)

@app.route('/logout')
def logout():
    return auth_controller.logout()

# Define admin api calls
@app.route('/admin/blog')
def admin_blog_view_all(id=None):
    return blog_controller.get(id, "admin")

@app.route('/admin/blog/<id>')
def admin_blog_view_one(id=None):
    return blog_controller.get(id, "admin", "ViewOne")

@app.route('/admin/blog/edit')
def admin_blog_edit_catch_bad_url():
    return redirect('/admin/blog')

@app.route('/admin/blog/edit/<id>')
def admin_blog_edit(id=None):
    return blog_controller.get(id, "admin", "Edit")

@app.route('/blog/update', methods = ['POST', 'GET'])
def blog_update():
    return blog_controller.update(request.method, request.form)

@app.route('/admin/blog/delete', methods = ['POST', 'GET'])
def admin_blog_delete():
    return blog_controller.delete(request.method, request.form)