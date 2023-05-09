from application import db, app
from application.models import Sensory
from flask import request, jsonify, render_template, redirect, url_for

def show_sensory():
    request_data = request.get_json()
    sensory_list = Sensory.query.filter_by( video_category = request_data.get("video_category")).all()
    data = [d.__dict__ for d in sensory_list]
    for item in data:
        item.pop('_sa_instance_state', None) 
    return data, 200
    # list = []
    # sensories = Sensory.query.all()
    # data = [d.__dict__ for d in sensories]
    # for item in data:
    #     item.pop('_sa_instance_state', None)    
    # return data, 200

