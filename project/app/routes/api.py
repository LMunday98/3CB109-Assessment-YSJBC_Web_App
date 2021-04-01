# api_routes.py

from flask import render_template, request, redirect

from models import *
from app import app
from app import login_manager, login_required, login_user

# Import all controllers
from app.controllers import *

# Login manager
@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    return render_template("auth/login.html", msg="Please login to continue!")
    
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
    return auth_controller.register(request.method, request.form)

@app.route('/logout')
def logout():
    return auth_controller.logout()

# Define admin api calls
@app.route('/admin/home')
@login_required
def admin_home():
    return render_template('admin/home.html')

@app.route('/admin/blog')
@login_required
def admin_blog_view_all(id=None):
    return blog_controller.get(id, "admin")

@app.route('/admin/blog/<id>')
@login_required
def admin_blog_view_one(id=None):
    return blog_controller.get(id, "admin", "ViewOne")

@app.route('/admin/blog/create')
@login_required
def admin_blog_create():
    return render_template('admin/blog.html', action="Create")

@app.route('/admin/blog/edit')
@login_required
def admin_blog_edit_catch_bad_url():
    return redirect('/admin/blog')

@app.route('/admin/blog/edit/<id>')
@login_required
def admin_blog_edit(id=None):
    return blog_controller.get(id, "admin", "Edit")

@app.route('/admin/blog/delete', methods = ['POST', 'GET'])
@login_required
def admin_blog_delete():
    return blog_controller.delete(request.method, request.form)

# Define admin blog api calls
@app.route('/blog/create', methods = ['POST', 'GET'])
@login_required
def blog_create():
    return blog_controller.create(request.method, request.form)

@app.route('/blog/update', methods = ['POST', 'GET'])
@login_required
def blog_update():
    return blog_controller.update(request.method, request.form)

# Admin user management calls
@app.route('/admin/users')
@app.route('/admin/users/<id>')
@login_required
def admin_users(id=None):
    return user_manager.get(id)

@app.route('/admin/users/delete', methods = ['POST', 'GET'])
@login_required
def admin_users_delete():
    return user_manager.delete(request.method, request.form)