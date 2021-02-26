from app.db import insert
from flask import render_template

def login(form_data):
    name = form_data['name']
    password = form_data['password']

    table = "users"
    fields = "user_name,user_password"
    data_types = "%s,%s"
    content = [name, password]

    data = [table, fields, data_types, content]
    insert(data)

    return render_template("index.html")