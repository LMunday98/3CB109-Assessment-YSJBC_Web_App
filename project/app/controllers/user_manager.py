from app.models.user import *
from flask import render_template, redirect

def get(user_id):
    if user_id == None:
        # Get all users
        users = User.query.all()
        return render_template('admin/user_manager.html', users=users)
    else:
        # Get specific user
        x=1
    return render_template('admin/user_manager.html', user_id=user_id)