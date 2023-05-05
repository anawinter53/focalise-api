from application import db, app
from application.models import Task
from flask import request, jsonify, render_template, redirect, url_for

def index_tasks_by_user(id):
    list = []
    tasks = Task.query.filter_by(user_id = id).all()
    for task in tasks:
        data = {
            "task_id": task.task_id,
            "user_id": task.user_id,
            "category_name": task.category_name,
            "task_name": task.task_name,
            "task_url": task.task_url,
            "task_desc": task.task_desc
        }
        list.append(data)

    return list, 200

def index_tasks_by_category(id, category):
    list = []
    tasks = Task.query.filter_by(user_id = id, category_name = category).all()
    for task in tasks:
        data = {
            "task_id": task.task_id,
            "user_id": task.user_id,
            "category_name": task.category_name,
            "task_name": task.task_name,
            "task_url": task.task_url,
            "task_desc": task.task_desc
        }
        list.append(data)

    return list, 200

def show_task(id):
    task = db.session.get(Task, id)
    return {
        "task_id": task.task_id,
        "user_id": task.user_id,
        "category_name": task.category_name,
        "task_name": task.task_name,
        "task_url": task.task_url,
        "task_desc": task.task_desc
    }


def create_task(id):
    data = request.get_json()
    user_id = id
    category_name = data.get('category_name')
    task_name = data.get('task_name')
    task_url = data.get('task_url')
    task_desc = data.get('task_desc')
    if not category_name or not task_name or not task_desc:
        return jsonify({'error': 'Missing parameters'}), 400
    task = Task(user_id=user_id, category_name=category_name, task_name=task_name, task_url=task_url, task_desc=task_desc)
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Successfully added a new task'}), 201

def update_task(id):
    data = request.get_json()
    task = db.session.get(Task, id)
    task.category_name = data.get('category_name')
    task.task_name = data.get('task_name')
    task.task_url = data.get('task_url')
    task.task_desc = data.get('task_desc')
    db.session.commit()
    return jsonify({'message': 'Task updated'})

def destroy_task(id):
    task = db.session.get(Task, id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted.'})