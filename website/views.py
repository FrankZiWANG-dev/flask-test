from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db
views = Blueprint("views", __name__)



@views.route("/", methods=["GET", "POST"])
def todos():
    todos = Todo.query.all()

    return render_template("todos.html", todos = todos)

@views.route("/add", methods=["GET", "POST"])
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        
        new_todo = Todo(title=title, content=content)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('views.todos'))

    return render_template("todos.html", todos = todos)

# @views.route("/edit-posts", methods=["GET", "POST"])
# def edit_posts():
#     if request.method == 'POST':
#         title = request.form.get('title')
#         url ='/edit-post?title='+title

#         return redirect(url)

#     return render_template("edit-posts.html")

# @views.route("/edit-post", methods=["GET", "POST"])
# def edit_post():
#     title = request.args.get('title')
#     post = Post.query.filter_by(title="test")
#     if request.method == 'POST':
#         post.title = request.form.get('title')
#         post.content = request.form.get('content')
#         post.image = request.form.get('image')
#         db.session.commit()
#         redirect='/dashboard'

#         return redirect(url_for(redirect))
    
#     return render_template("edit-post.html", former_title=post.title, former_content=post.content, former_image=post.image)