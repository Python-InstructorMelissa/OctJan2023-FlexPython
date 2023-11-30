from app import app
from flask import render_template, request, redirect

from app.models.task import Task

@app.route("/task/add")
def get_add_task_form():
    return render_template("add_task.html")

@app.route("/task/add", methods=["POST"]) # When to redirect. After updating the database
def add_task():
    form_data = request.form
    print(form_data)
    Task.add(form_data)
    return redirect('/task/add')
