from flask import Blueprint
from application.controllers.settingController import *

setting_routes = Blueprint("setting_routes", __name__)

@setting_routes.route('/<int:user_id>')
def get_settings(user_id):
    return show_settings(user_id)

@setting_routes.route('/<int:user_id>', methods=['PUT'])
def update_settings_route(user_id):
    return update_settings(user_id)
