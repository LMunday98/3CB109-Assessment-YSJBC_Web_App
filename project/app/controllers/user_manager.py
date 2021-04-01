from app.models.user import *
from flask import render_template, redirect

def get(user_id, msg=None):
    if user_id == None:
        # Get all users
        all_users = User.query.all()
        approved_users = User.query.filter_by(account_type='user').all()
        guest_users = User.query.filter_by(account_type='guest').all()
        return render_template('admin/user_manager.html', all_users=all_users, approved_users=approved_users, guest_users=guest_users, msg=msg)
    else:
        # Get specific user
        x=1
    return render_template('admin/user_manager.html', user_id=user_id)

def approve(method, form_data):
    if (method == 'POST') :
        try:
            user = User.get_user_by_id(form_data['approve_id'])
            user.set_account_type('user')
            return view_page(user.email + ' has been approved!')
        except Exception as e:
            return view_page(e)
    return view_page('Error approving account!')

def unapprove(method, form_data):
    if (method == 'POST') :
        try:
            user = User.get_user_by_id(form_data['unapprove_id'])
            user.set_account_type('guest')
            return view_page(user.email + ' has been unapproved!')
        except Exception as e:
            return view_page(e)
    return view_page('Error unapproving account!')

def delete(method, form_data):
    if (method == 'POST') :
        try:
            User.delete(form_data['delete_id'])
            return view_page('Account successfully deleted!')
        except Exception as e:
            return view_page(e)
    return view_page('Error deleting account!')

def view_page(message):
    return get(None, message)