from app.db import insert
from flask import render_template

def register(form_data):

    email = form_data['email']
    password = form_data['password']
    confirm_password = form_data['password_confirm']

    if (not email or not password):
        return render_template("form.html", msg="Please fill out all fields.")

    table = "users"
    fields = "user_name,user_password"
    data_types = "%s,%s"
    content = [email, password]

    data = [table, fields, data_types, content]
    insert(data)

    return render_template("index.html")