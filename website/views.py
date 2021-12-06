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

@views.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == 'POST':
        id_edit = request.form.get('id-edit')
        old_todo = Todo.query.filter_by(id=id_edit).first()
        if old_todo:
            db.session.delete(old_todo)
            db.session.commit()

            title = request.form.get('title-edit')
            content = request.form.get('content-edit')
            
            edited_todo = Todo(id=id_edit, title=title, content=content)
            db.session.add(edited_todo)
            db.session.commit()
            return redirect(url_for('views.todos'))

        return redirect(url_for('views.todos'))

    return render_template("todos.html", todos = todos)

@views.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == 'POST':
        id_delete = request.form.get('id-delete')
        todo_delete = Todo.query.filter_by(id=id_delete).first()
        if todo_delete:
            db.session.delete(todo_delete)
            db.session.commit()

        return redirect(url_for('views.todos'))

    return render_template("todos.html", todos = todos)