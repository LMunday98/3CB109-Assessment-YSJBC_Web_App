from app.models.user import *
from flask import render_template, redirect

def login(form_data):
    
    email = form_data['email']
    password = form_data['password']

    user = get_user(email)

    if ((user != None) and (user.check_password(password))):
        return render_template("admin/home.html", msg="Email or password was incorrect!")
    else:
        return render_template("user/login.html", msg="Email or password was incorrect!")

    

def register(form_data):

    email = form_data['email']
    password = form_data['password']
    confirm_password = form_data['password_confirm']

    if (not (email or password or confirm_password) ):
        return render_template("user/register.html", msg="Please fill out all fields!")

    if (not (password == confirm_password) ):
        return render_template("user/register.html", msg="Passwords do not match!")

    #if (user_exist(email)):
        #return render_template("user/register.html", msg="User already exists!")

    create_user(email, password)

    return render_template("user/login.html", msg="User account successfully created!")

def logout():
    # logout stuff
    return redirect("/")