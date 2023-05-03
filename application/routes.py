from application import app, db
from application.models import User
from flask import request, jsonify, render_template, redirect, url_for

@app.route('/')
def welcome():
    return "Welcome to the API!"


@app.route('/users')
def index():
    list = []
    users = User.query.all()
    for user in users:
        data = {
            "id": user.user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        }
        list.append(data)

    return list, 200

@app.route('/users/new', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if not username or not email or not password:
        return jsonify({'error': 'Missing parameters'}), 400
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Successfully created new user'}), 201


