from application import db
from application.models.models import Message
from flask import request, jsonify, render_template, redirect, url_for

def index_messages():
    list = []
    messages = Message.query.order_by(Message.date.asc()).all()
    data = [d.__dict__ for d in messages]
    for item in data:
        item.pop('_sa_instance_state', None)
    return data, 200
