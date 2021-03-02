from app.models.blog import *
from flask import render_template, redirect

def update(form_data):
    title = form_data['title']
    desc = form_data['desc']
    body = form_data['body']

    print ("Title: " + title + "\n")
    print ("Desc: " + desc + "\n")
    print ("Body: " + body + "\n")

    return redirect('/admin/blog')