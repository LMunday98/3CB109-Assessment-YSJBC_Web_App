from app.models.blog import *
from flask import render_template, redirect, request

import os

def create(method, form_data):
    if method == 'POST':
        try:
            # Get form data
            new_title = form_data['title']
            new_desc = form_data['desc']
            new_body = form_data['body']
            uploaded_file = request.files['thumbnail']

            # Check if the user uploaded an image
            if uploaded_file.filename != '':
                # Save the image with the blog id, then save the image to the server and store the path in the blog db
                latest_blog = Blog.query.order_by(Blog.id.desc()).first()
                new_file_name = 'blog' + str(int(latest_blog.id) + 1)
                new_file_ext = '.' + uploaded_file.filename.split('.')[-1]

                # use the the file extension of the uploaded file and join to the new name, given by the blog id and save
                new_file_path = new_file_name + new_file_ext
                uploaded_file.save('app/static/blog_thumbnails/' + new_file_path)

            # Create the blog
            Blog.create(new_title, new_desc, new_body, new_file_path)
        except Exception as e:
            return(str(e))

    return redirect('/admin/blog')

def update(method, form_data):
    if method == 'POST':
        try:
            # Get form data
            id = form_data['id']
            new_title = form_data['title']
            new_desc = form_data['desc']
            new_body = form_data['body']
            uploaded_file = request.files['thumbnail']

            # Get the referenced blog
            current_blog = Blog.get(id)

            # Check if the user uploaded a new file, if not skip
            # If they did, then overwrite the currently existsing file
            # No need to update the thumbnail name in the db as it will be the same
            if uploaded_file.filename != '':
                new_file_path = current_blog.thumbnail
                uploaded_file.save('app/static/blog_thumbnails/' + new_file_path)

            # Update the blog
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
            # Get form data
            # First delete image, then delete blog
            id = form_data['delete_id']
            delete_blog = Blog.get(id)
            thumbnail_path = delete_blog.thumbnail
            os.remove('app/static/blog_thumbnails/' + thumbnail_path)
            Blog.delete(id)
        except Exception as e:
            return(str(e))

    return redirect('/admin/blog')