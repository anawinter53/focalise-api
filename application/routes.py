from application import app, db
from application.models import Users
from flask import request, jsonify, render_template, redirect, url_for

@app.route('/')
def hello():
    return "Hey!"
