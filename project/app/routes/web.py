# web_routes.py

from flask import render_template, request, redirect

from models import *
from app import app

# Define public routes
@app.route('/')
def index():
    recent_blogs = Blog.query.order_by(Blog.updated_at.desc()).limit(3).all()
    return render_template("public/index.html", recent_blogs=recent_blogs)

@app.route('/about')
def about():
    return render_template("public/about.html")

@app.route('/blog')
@app.route('/blog/<id>')
def blog(id=None):
    blog = Blog.get_blog(id)
    if (blog != None):
        # Get specific blog
        return render_template('public/blog.html', blog=blog)
    else:
        # Display all
        blogs = Blog.query.all()
        return render_template('public/blog.html', blogs=blogs)
    

@app.route('/training')
def training():
    return render_template("public/training.html")

@app.route('/contact')
def contact():
    return render_template("public/contact.html")

# Define auth routes
@app.route('/auth/login')
def user_login():
    return render_template("auth/login.html")

@app.route('/auth/register')
def user_register():
    return render_template("auth/register.html")

# Define admin routes
@app.route('/admin/home')
def admin_home():
    return render_template('admin/home.html')

@app.route('/admin/blog')
@app.route('/admin/blog/<id>')
def admin_blog(id=None):
    blog = Blog.get_blog(id)
    if (blog != None):
        # Get specific blog
        return render_template('admin/blog.html', blog=blog, action="ViewOne")
    else:
        # Display all
        blogs = Blog.query.all()
        return render_template('admin/blog.html', blogs=blogs, action="ViewAll")

@app.route('/admin/blog/edit')
@app.route('/admin/blog/edit/<id>')
def admin_blog_edit(id=None):
    blog = Blog.get_blog(id)
    if (blog != None):
        # Get specific blog
        return render_template('admin/blog.html', blog=blog, action="Edit")
    else:
        # Return to all blogs
        return redirect('/admin/blog')

@app.route('/admin/blog/delete', methods = ['POST', 'GET'])
def admin_blog_delete():
    if ((request.method == 'POST')) :
        try:
            Blog.delete_blog(request.form['delete_id'])
        except Exception as e:
            return(str(e))

    return redirect('/admin/blog')