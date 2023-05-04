from application import app, db
from application.models import User
from flask import Blueprint
from application.controllers.sensoryController import *

sensory_routes = Blueprint("sensory_routes", __name__)

@sensory_routes.route('/')
def get_sensory():
    return show_sensory()
