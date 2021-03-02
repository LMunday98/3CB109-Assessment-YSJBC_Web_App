from app.models.blog import *
from flask import render_template, redirect

def create(method, form_data):
    if method == 'POST':
        try:
            new_title = form_data['title']
            new_desc = form_data['desc']
            new_body = form_data['body']
            Blog.create(new_title, new_desc, new_body)
        except Exception as e:
            return(str(e))

    return redirect('/admin/blog')

def update(method, form_data):
    if method == 'POST':
        try:
            id = form_data['id']
            new_title = form_data['title']
            new_desc = form_data['desc']
            new_body = form_data['body']

            current_blog = Blog.get(id)
            current_blog.update(new_title, new_desc, new_body)
        except Exception as e:
            return(str(e))

    return redirect('/admin/blog')

def get(id, route, action="ViewAll"):
    try:
        url = route + '/blog.html'
        blog = Blog.get(id)
        if (blog != None):
            # Get specific blog
            return render_template(url, blog=blog, action=action)
        else:
            # Display all
            blogs = Blog.query.order_by(Blog.updated_at.desc()).all()
            return render_template(url, blogs=blogs, action="ViewAll")
    except Exception as e:
        return(str(e))
    
def delete(method, form_data):
    if (method == 'POST') :
        try:
            Blog.delete(form_data['delete_id'])
        except Exception as e:
            return(str(e))

    return redirect('/admin/blog')