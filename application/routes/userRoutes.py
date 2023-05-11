from application import app, db
from flask import Blueprint
from application.controllers.userController import *

user_routes = Blueprint("user_routes", __name__)

@user_routes.route('/')
def index_users_route():
    return index_users()

@user_routes.route('/register', methods=['POST'])
def create_user_route():
    return register()

@user_routes.route('/login', methods=['POST'])
def login_route():
    return login()

@user_routes.route('/logout', methods=['POST'])
def logout_route():
    return logout()

@user_routes.route('/<int:user_id>')
def show_user_route(user_id):
    return show_user(user_id)

@user_routes.route('/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    return update_user_details(user_id)

@user_routes.route('password/<int:user_id>', methods=['PUT'])
def update_password_route(user_id):
    return update_user_password(user_id)

@user_routes.route('password/<int:user_id>', methods=['POST'])
def check_password_route(user_id):
    return check_password(user_id)