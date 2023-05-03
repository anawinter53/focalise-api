from application import app, db
from application.models import User
from flask import request, jsonify, render_template, redirect, url_for
from application.controllers import *

@app.route('/')
def welcome():
    return "Welcome to the API!"


@app.route('/users')
def index_users_route():
    return index_users()


@app.route('/users/new', methods=['POST'])
def create_user_route():
    return create_user()

@app.route('/users/<int:user_id>')
def show_user_route(user_id):
    return show_user(user_id)

@app.route('/users/<int:user_id>/tasks')
def get_users_tasks(user_id):
    return index_tasks_by_user(user_id)

@app.route('/users/<int:user_id>/new_task', methods=['POST'])
def add_new_task(user_id):
    return create_task(user_id)

