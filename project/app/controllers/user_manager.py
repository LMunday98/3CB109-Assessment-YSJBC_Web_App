from app.models.user import *
from flask import render_template, redirect

def get(user_id, msg='', msg_colour=None):
    if user_id == None:
        # Get all users
        all_users = User.query.all()
        approved_users = User.query.filter_by(account_type='user').all()
        guest_users = User.query.filter_by(account_type='guest').all()
        return render_template('admin/user_manager.html', all_users=all_users, approved_users=approved_users, guest_users=guest_users, msg=msg, msg_colour=msg_colour)
    else:
        # Get specific user
        x=1
    return render_template('admin/user_manager.html', user_id=user_id)

def approve(method, form_data):
    if (method == 'POST') :
        try:
            # find and approve user by given id
            user = User.get_user_by_id(form_data['approve_id'])
            user.set_account_type('user')
            return view_page(user.email + ' has been approved!', 'green')
        except Exception as e:
            return view_page(e, 'red')
    return view_page('Error approving account!', 'red')

def unapprove(method, form_data):
    if (method == 'POST') :
        try:
            # find and unapprove user by given id
            user = User.get_user_by_id(form_data['unapprove_id'])
            user.set_account_type('guest')
            return view_page(user.email + ' has been unapproved!', 'green')
        except Exception as e:
            return view_page(e, 'red')
    return view_page('Error unapproving account!', 'red')

def delete(method, form_data):
    if (method == 'POST') :
        try:
            # get form data and delete user
            User.delete(form_data['delete_id'])
            return view_page('Account successfully deleted!', 'green')
        except Exception as e:
            return view_page(e, 'red')
    return view_page('Error deleting account!', 'red')

def view_page(message, msg_colour):
    # used to apply colour to messages
    if msg_colour == 'red':
        msg_colour = 'danger'
    if msg_colour == 'green':
        msg_colour = 'success'
    return get(None, message, msg_colour)