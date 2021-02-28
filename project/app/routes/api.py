# api_routes.py

from flask import render_template, request

from models import *
from app import app

# Import all controllers
from app.controllers import *

# Define user api calls
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
     
    if request.method == 'POST':
        try:
            return auth.login(request.form)
        except Exception as e:
            return(str(e))

@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('user/register.html')
     
    if request.method == 'POST':
        try:
            return auth.register(request.form)
        except Exception as e:
            return(str(e))

@app.route('/logout')
def logout():
    try:
        return auth.logout()
    except Exception as e:
        return(str(e))

# Define admin api calls
@app.route('/admin/home')
def admin_home():
    try:
        users = User.query.all()
        return render_template('admin/home.html', users=users)
    except Exception as e:
        return(str(e))





@app.route('/dessert/view')
def dessert_view():
    try:
        desserts = Dessert.query.all()
        return render_template('dessert.html', desserts=desserts)
    except Exception as e:
        return(str(e))

@app.route('/dessert/add', methods=['GET', 'POST'])
def dessert_add():

    if request.method == 'GET':
        return render_template('add.html')

    dessert_name = request.form.get('name_field')
    dessert_price = request.form.get('price_field')
    dessert_cals = request.form.get('cals_field')

    dessert = create_dessert(dessert_name, dessert_price, dessert_cals)
    return render_template('add.html', dessert=dessert)