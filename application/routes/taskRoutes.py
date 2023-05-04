from application import app, db
from flask import Blueprint
from application.controllers.taskController import *

task_routes = Blueprint("task_routes", __name__)

@task_routes.route('/<int:user_id>')
def get_users_tasks(user_id):
    return index_tasks_by_user(user_id)

@task_routes.route('/<int:user_id>/<category>')
def get_tasks_by_category(user_id, category):
    return index_tasks_by_category(user_id, category)

@task_routes.route('/<int:user_id>', methods=['POST'])
def add_new_task(user_id):
    return create_task(user_id)
