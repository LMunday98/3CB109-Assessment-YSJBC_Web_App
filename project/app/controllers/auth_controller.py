import flask
import logging
from flask import render_template, redirect
from app.models.user import *
from flask_login import login_user, current_user, logout_user

def login(method, form_data):
    if method == 'POST':
        try:
            # Get form data
            email = form_data['email']
            password = form_data['password']
            user = User.get(email)

            # Check if user account has been approved by an admin
            if ((user != None) and (user.check_password(password))):
                if (not user.check_verified()):
                    return render_template("auth/login.html", msg="Account has not been approved!")
                    
                # Login manager authenticate user
                login_user(user)
                flask.flash('Logged in successfully.')
                next = flask.request.args.get('next')
                
                if not is_safe_url(next):
                    return flask.abort(400)

                # Navigate user to appropriate page, depending on account type and permissions level
                account_type = user.account_type
                # return render_template(account_type + "/home.html", msg="Logged in!")
                return redirect(account_type + "/home")
            else:
                return render_template("auth/login.html", msg="Email or password was incorrect!")

        except Exception as e:
            return(str(e))

    return render_template('auth/login.html')

def register(method, form_data):
    if method == 'POST':
        try:
            # Get form data
            email = form_data['email']
            password = form_data['password']
            confirm_password = form_data['password_confirm']

            # Check if passwords match
            if (not (password == confirm_password) ):
                return render_template("auth/register.html", msg="Passwords do not match!")

            # Get any users with the email provided
            user = User.get(email)

            # Check if account already exists
            if (user != None):
                return render_template("auth/register.html", msg="User already exists!")

            # Create user then navigate to login page with msg
            User.create(email, password)
            return render_template("auth/login.html", msg="User account successfully created!")
            
        except Exception as e:
            return(str(e))

    return render_template('auth/register.html')

# Check if the account type is admin
def check_admin(current_user):
    if current_user.account_type == 'admin':
        return True
    return False

def logout():
    # logout stuff
    try:
        print ('logout')
        logout_user()
    except Exception as e:
        return(str(e))

    return redirect("/")

def is_safe_url(next_url):
    #logger.debug("next url is %s:" % next_url)
    return True