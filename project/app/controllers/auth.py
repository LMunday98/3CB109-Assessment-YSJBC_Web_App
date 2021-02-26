from app.controllers.db_ops import *
from flask import render_template, redirect

def login(form_data):
    
    email = form_data['email']
    password = form_data['password']

    if (not (email or password) ):
        return render_template("form.html", msg="Please fill out all fields!")

    data = [email]
    return user_exist(data)

    return render_template("index.html")

def register(form_data):

    email = form_data['email']
    password = form_data['password']
    confirm_password = form_data['password_confirm']

    if (not (email or password or confirm_password) ):
        return render_template("user/register.html", msg="Please fill out all fields!")

    if (not (password == confirm_password) ):
        return render_template("user/register.html", msg="Passwords do not match!")

    if (not user_exist(email)):
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