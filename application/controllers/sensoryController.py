from application import db, app
from application.models import Sensory
from flask import request, jsonify, render_template, redirect, url_for

def show_sensory():
    list = []
    sensories = Sensory.query.all()
    for s in sensories:
        data = {
            "sensory_id": s.sensory_id,
            "video_category": s.video_category,
            "video_url": s.video_url
        }
        list.append(data)
    return list, 200

