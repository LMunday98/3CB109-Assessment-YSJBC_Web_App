from app.controllers.db_ops import *
from flask import render_template, redirect

def login(form_data):
    
    email = form_data['email']
    password = form_data['password']

    if (not (email or password) ):
        return render_template("admin/login.html", msg="Please fill out all fields!")

    if (not user_exist(email)):
        return render_template("admin/login.html", msg="Email or password was incorrect!")

    results = get_user(email)
    found_user_email = results[1]
    found_user_password = results[2]

    if ((email == found_user_email) and (password == found_user_password)):
        return render_template("admin/home.html", msg="logged in")
    else:
        return render_template("admin/login.html", msg="Email or password was incorrect!")

    

def register(form_data):

    email = form_data['email']
    password = form_data['password']
    confirm_password = form_data['password_confirm']

    if (not (email or password or confirm_password) ):
        return render_template("user/register.html", msg="Please fill out all fields!")

    if (not (password == confirm_password) ):
        return render_template("user/register.html", msg="Passwords do not match!")

    if (user_exist(email)):
        return render_template("user/register.html", msg="User already exists!")

    table = "users"
    fields = "user_email,user_password"
    data_types = "%s,%s"
    content = [email, password]

    data = [table, fields, data_types, content]
    insert(data)

    return render_template("user/login.html", msg="User account successfully created!")

def logout():
    # logout stuff
    return redirect("/")