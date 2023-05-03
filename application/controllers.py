from application import db, app
from application.models import User, UserSetting, Task, Message, Token
from flask import request, jsonify, render_template, redirect, url_for

def index_users():
    list = []
    users = User.query.all()
    for user in users:
        data = {
            "id": user.user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        }
        list.append(data)

    return list, 200

def show_user(id):
    user = User.query.filter_by(user_id = id).first()
    return {
        "id": user.user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password
    }

def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Missing parameters'}), 400
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Successfully created new user'}), 201


def index_tasks_by_user(id):
    list = []
    tasks = Task.query.filter_by(user_id = id).all()
    for task in tasks:
        data = {
            "task_id": task.task_id,
            "user_id": task.user_id,
            "category_name": task.category_name,
            "task_name": task.task_name,
            "task_url": task.task_url
        }
        list.append(data)

    return list, 200

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
    return jsonify({'message': 'Successfully added a new'}), 201