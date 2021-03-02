from app.models.user import *
from flask import render_template, redirect

def login(method, form_data):
    if request.method == 'POST':
        try:
            email = form_data['email']
            password = form_data['password']
            user = User.get(email)

            if ((user != None) and (user.check_password(password))):
                account_type = user.account_type
                return render_template(account_type + "/home.html", msg="Logged in!")
            else:
                return render_template("auth/login.html", msg="Email or password was incorrect!")

        except Exception as e:
            return(str(e))

    return render_template('auth/login.html')

def register(method, form_data):
    if request.method == 'POST':
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
    except Exception as e:
        return(str(e))

    return redirect("/")