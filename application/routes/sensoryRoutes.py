from application import app, db
from flask import Blueprint
from application.controllers.sensoryController import *

sensory_routes = Blueprint("sensory_routes", __name__)

@sensory_routes.route('/')
def get_sensory():
    return index_sensory()

@sensory_routes.route('/<category>')
def get_senosry_by_category(category):
    return index_sensory_by_category(category)

@sensory_routes.route('/id/<int:sensory_id>')
def get_sensory_by_id(sensory_id):
    return show_sensory(sensory_id)
