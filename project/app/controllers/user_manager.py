from app.models.user import *
from flask import render_template, redirect

def get(id):
    return render_template('admin/user_manager.html', user_id=id)