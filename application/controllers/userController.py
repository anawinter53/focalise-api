from application import db, app
from application.models import User, UserSetting, Token
from flask import request, jsonify, render_template, redirect, url_for
import bcrypt
import os
from uuid import uuid4

def index_users():
    list = []
    users = User.query.all()
    for user in users:
        data = {
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "password": user.password
        }
        list.append(data)

    return list, 200

def show_user(id):
    user = db.session(User, id)
    return {
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password
    }

def get_user_by_username(name):
    user = User.query.filter_by(username = name).first()
    return {
        "user_id": user.user_id,
        "username": user.username,
        "email": user.email,
        "password": user.password
    }, 200

def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password').encode('utf-8')
    salt = bcrypt.gensalt(rounds=int(os.getenv("SALT_ROUNDS")))
    hashed_password = bcrypt.hashpw(password, salt).decode('utf-8')
    if not username or not email or not password:
        return jsonify({'error': 'Missing parameters'}), 400
    user = User(username=username, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    user = get_user_by_username(username)
    settings = UserSetting(user_id=user.get('user_id'))
    db.session.add(settings)
    db.session.commit()
    return jsonify({'message': 'Successfully created new user'}), 201

def login():
    data = request.get_json()
    user = get_user_by_username(data.get('username'))
    authenticated = bcrypt.checkpw(data.get('password').encode('utf-8'), user.get('password').encode('utf-8'))
    if not authenticated:
        return jsonify({'error': 'Incorrect credentials'}), 403
    token = create_token(user.get('user_id'))
    return jsonify({'authenticated': authenticated, 'token': token.token, 'id': user.get('user_id')}), 200

def logout():
    data = request.get_json()
    token = Token.query.filter_by(token = data.get('token')).first()
    db.session.delete(token)
    db.session.commit()
    return jsonify({'message': 'Token deleted'})

def create_token(id):
    token = uuid4()
    if not id or not token:
        return jsonify({'message': 'Missing parameters'})
    newToken = Token(user_id=id, token=token)
    db.session.add(newToken)
    db.session.commit()
    return newToken