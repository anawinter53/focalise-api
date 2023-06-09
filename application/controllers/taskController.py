from application import db, app
from application.models import Task
from flask import request, jsonify, render_template, redirect, url_for

def index_tasks_by_user(id):
    tasks = Task.query.filter_by(user_id = id).order_by(Task.task_deadline.desc()).all()
    data = [d.__dict__ for d in tasks]
    for item in data:
        item.pop('_sa_instance_state', None) 

    return data, 200

def index_tasks_by_category(id, category):
    tasks = Task.query.filter_by(user_id = id, category_name = category).order_by(Task.task_deadline.desc()).all()
    data = [d.__dict__ for d in tasks]
    for item in data:
        item.pop('_sa_instance_state', None) 

    return data, 200

def index_categories_by_user(id):
    tasks = Task.query.filter_by(user_id = id).all()
    list = []
    for t in tasks:
        if t.category_name not in list:
            list.append(t.category_name)
    return list, 200

def index_tasks_by_status(id, category, status):
    tasks = Task.query.filter_by(user_id = id, category_name=category, task_status = status).order_by(Task.task_deadline.desc()).all()
    data = [d.__dict__ for d in tasks]
    for item in data:
        item.pop('_sa_instance_state', None)
    return data, 200    

def show_task(id):
    task = db.session.get(Task, id).__dict__
    task.pop('_sa_instance_state', None)
    return jsonify(task)


def create_task(id):
    data = request.get_json()
    user_id = id
    category_name = data.get('category_name')
    task_name = data.get('task_name')
    task_url = data.get('task_url')
    task_desc = data.get('task_desc')
    task_deadline = data.get('task_deadline')
    if not category_name or not task_name or not task_desc:
        return jsonify({'error': 'Missing parameters'}), 400
    task = Task(user_id=user_id, category_name=category_name, task_name=task_name, task_url=task_url, task_desc=task_desc, task_deadline=task_deadline)
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
    task.task_deadline = data.get('task_deadline')
    # task.task_status = data.get('task_status')
    db.session.commit()
    return jsonify({'message': 'Task updated'})

def update_task_status(id):
    data = request.get_json()
    task = db.session.get(Task, id)
    task.task_status = data.get('task_status')
    db.session.commit()
    return jsonify({'message': "Status updated"})

def destroy_task(id):
    task = db.session.get(Task, id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted.'})

def destroy_task_by_category(user_id, category):
    tasks = index_tasks_by_category(user_id, category)
    for t in tasks[0]:
        task = db.session.get(Task, t.get('task_id'))
        db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Category deleted'})