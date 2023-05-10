from application import app, db
from flask import Blueprint
from application.controllers.taskController import *

task_routes = Blueprint("task_routes", __name__)

@task_routes.route('/user/<int:user_id>')
def get_users_tasks(user_id):
    return index_tasks_by_user(user_id)

@task_routes.route('/user/<int:user_id>/<category>')
def get_tasks_by_category(user_id, category):
    return index_tasks_by_category(user_id, category)

@task_routes.route('/user/<int:user_id>/categories')
def get_categories_by_user(user_id):
    return index_categories_by_user(user_id)

@task_routes.route('/user/<int:user_id>/status/<status>')
def get_tasks_by_status(user_id, status):
    return index_tasks_by_status(user_id, status)

@task_routes.route('/user/<int:user_id>', methods=['POST'])
def add_new_task(user_id):
    return create_task(user_id)

@task_routes.route('/<int:task_id>')
def get_task(task_id):
    return show_task(task_id)

@task_routes.route('/<int:task_id>', methods=['PUT'])
def update_task_route(task_id):
    return update_task(task_id)

@task_routes.route('/<int:task_id>', methods=['DELETE'])
def destroy_task_route(task_id):
    return destroy_task(task_id)

@task_routes.route('/user/<int:user_id>/<category>', methods=['DELETE'])
def destroy_task_by_category_route(user_id, category):
    return destroy_task_by_category(user_id, category)