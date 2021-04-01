from app.models.user import *
from flask import render_template, redirect

def get(user_id):
    if user_id == None:
        # Get all users
        all_users = User.query.all()
        approved_users = User.query.filter_by(account_type='user').all()
        guest_users = User.query.filter_by(account_type='guest').all()
        return render_template('admin/user_manager.html', all_users=all_users, approved_users=approved_users, guest_users=guest_users)
    else:
        # Get specific user
        x=1
    return render_template('admin/user_manager.html', user_id=user_id)

def delete(method, form_data):
    if (method == 'POST') :
        try:
            User.delete(form_data['delete_id'])
        except Exception as e:
            return(str(e))

    return redirect('/admin/users')