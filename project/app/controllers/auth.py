from app.db import connection
from flask import render_template

def login(form_data):
    name = form_data['name']
    password = form_data['password']

    cursor, conn = connection()
    cursor.execute("insert into users (user_name,user_password) values(%s,%s)", (name,password))
    conn.commit()
    cursor.close()

    return render_template("index.html")