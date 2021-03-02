from app.models.blog import *
from flask import render_template, redirect

def update(form_data):
    id = form_data['id']
    new_title = form_data['title']
    new_desc = form_data['desc']
    new_body = form_data['body']

    current_blog = Blog.get_blog(id)
    current_blog.update_blog(new_title, new_desc, new_body)

    return redirect('/admin/blog')