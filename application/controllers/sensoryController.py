from application import db, app
from application.models import Sensory
from flask import request, jsonify, render_template, redirect, url_for

def show_sensory(id):
    sensory = db.session.get(Sensory, id).__dict__
    sensory.pop('_sa_instance_state', None) 
    return jsonify(sensory), 200

def index_sensory():
    sensories = Sensory.query.all()
    data = [d.__dict__ for d in sensories]
    for item in data:
        item.pop('_sa_instance_state', None)    
    return data, 200

def index_sensory_by_category(category):
    sensories = Sensory.query.filter_by(video_category = category).all()
    data = [d.__dict__ for d in sensories]
    for item in data:
        item.pop('_sa_instance_state', None)    
    return data, 200

