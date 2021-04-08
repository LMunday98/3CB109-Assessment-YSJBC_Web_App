import flask
import logging
from flask import render_template, redirect
from app.models.user import *
from flask_login import login_user, current_user, logout_user

def login(method, form_data):
    if method == 'POST':
        try:
            email = form_data['email']
            password = form_data['password']
            user = User.get(email)

            if ((user != None) and (user.check_password(password))):
                if (not user.check_verified()):
                    return render_template("auth/login.html", msg="Account has not been approved!")
                    
                # Login manager authenticate user
                login_user(user)
                flask.flash('Logged in successfully.')
                next = flask.request.args.get('next')
                
                if not is_safe_url(next):
                    return flask.abort(400)

                account_type = user.account_type
                return render_template(account_type + "/home.html", msg="Logged in!")
            else:
                return render_template("auth/login.html", msg="Email or password was incorrect!")

        except Exception as e:
            return(str(e))

    return render_template('auth/login.html')

def register(method, form_data):
    if method == 'POST':
        try:
            email = form_data['email']
            password = form_data['password']
            confirm_password = form_data['password_confirm']

            if (not (password == confirm_password) ):
                return render_template("auth/register.html", msg="Passwords do not match!")

            user = User.get(email)

            if (user != None):
                return render_template("auth/register.html", msg="User already exists!")

            User.create(email, password)
            return render_template("auth/login.html", msg="User account successfully created!")
            
        except Exception as e:
            return(str(e))

    return render_template('auth/register.html')

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