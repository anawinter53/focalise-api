from flask import Blueprint
from application.controllers.messageController import *

message_routes = Blueprint("message_routes", __name__)

@message_routes.route('/')
def get_messages():
    return index_messages()
