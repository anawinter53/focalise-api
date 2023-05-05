from application import db, app
from application.models import Sensory
from flask import request, jsonify, render_template, redirect, url_for

def show_sensory():
    list = []
    sensories = Sensory.query.all()
    data = [d.__dict__ for d in sensories]
    for item in data:
        item.pop('_sa_instance_state', None)    
    return data, 200

