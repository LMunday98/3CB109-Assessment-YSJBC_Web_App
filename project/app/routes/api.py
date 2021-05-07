# api_routes.py

from flask import render_template, request, redirect

from models import *
from app import app
from app import login_manager, login_required, login_user
from flask_login import login_user, current_user, logout_user

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




# Define user api calls
@app.route('/user/home')
@login_required
def user_home():
    # return render_template('user/home.html')
    return redirect('/user/training')

@app.route('/user/training', methods = ['POST', 'GET'])
@login_required
def user_training():
    return event_controller.show('/user', request.method, request.form)




# Define admin api calls
@app.route('/admin/home')
@login_required
def admin_home():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    # return render_template('admin/home.html')
    return redirect('/admin/users')

@app.route('/admin/blog')
@login_required
def admin_blog_view_all(id=None):
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return blog_controller.get(id, "admin")

@app.route('/admin/blog/<id>')
@login_required
def admin_blog_view_one(id=None):
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return blog_controller.get(id, "admin", "ViewOne")

@app.route('/admin/blog/create')
@login_required
def admin_blog_create():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return render_template('admin/blog.html', action="Create")

@app.route('/admin/blog/edit')
@login_required
def admin_blog_edit_catch_bad_url():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return redirect('/admin/blog')

@app.route('/admin/blog/edit/<id>')
@login_required
def admin_blog_edit(id=None):
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return blog_controller.get(id, "admin", "Edit")

@app.route('/admin/blog/delete', methods = ['POST', 'GET'])
@login_required
def admin_blog_delete():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return blog_controller.delete(request.method, request.form)





# Define admin blog api calls
@app.route('/blog/create', methods = ['POST', 'GET'])
@login_required
def blog_create():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return blog_controller.create(request.method, request.form)

@app.route('/blog/update', methods = ['POST', 'GET'])
@login_required
def blog_update():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return blog_controller.update(request.method, request.form)




# Admin user management calls
@app.route('/admin/users')
@app.route('/admin/users/<id>')
@login_required
def admin_users(id=None):
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return user_manager.get(id)

@app.route('/admin/users/delete', methods = ['POST', 'GET'])
@login_required
def admin_users_delete():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return user_manager.delete(request.method, request.form)

@app.route('/admin/users/approve', methods = ['POST', 'GET'])
@login_required
def admin_users_approve():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return user_manager.approve(request.method, request.form)

@app.route('/admin/users/unapprove', methods = ['POST', 'GET'])
@login_required
def admin_users_unapprove():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return user_manager.unapprove(request.method, request.form)




# Define admin training api calls
@app.route('/admin/training', methods = ['POST', 'GET'])
@login_required
def admin_training():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return event_controller.show('/admin', request.method, request.form)

@app.route('/admin/training/create', methods=['GET', 'POST'])
@login_required
def admin_event_create():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return event_controller.create(request.method, request.form)

@app.route('/admin/training/edit')
@login_required
def admin_training_edit_catch_bad_url():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return redirect('/admin/training')

@app.route('/admin/training/edit/<id>')
@login_required
def admin_training_edit(id=None):
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return event_controller.edit(id)

@app.route('/admin/training/update', methods = ['POST', 'GET'])
@login_required
def admin_training_update():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return event_controller.update(request.method, request.form)

@app.route('/admin/training/delete', methods = ['POST', 'GET'])
@login_required
def admin_training_delete():
    if not auth_controller.check_admin(current_user):
        return render_template("auth/login.html", msg="You don't have the required permissions to access that page!")
    return event_controller.delete(request.method, request.form)