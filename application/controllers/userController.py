from application import db, app
from application.models import User, UserSetting, Token
from flask import request, jsonify, render_template, redirect, url_for
import bcrypt
import os
from uuid import uuid4

def index_users():
    users = User.query.all()
    data = [d.__dict__ for d in users]
    for item in data:
        item.pop('_sa_instance_state', None)
    return data, 200

def show_user(id):
    user = db.session.get(User, id).__dict__
    user.pop('_sa_instance_state', None)
    return jsonify(user)

def get_user_by_username(name):
    user = User.query.filter_by(username = name).first().__dict__
    user.pop('_sa_instance_state', None)
    return jsonify(user)

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
    user = get_user_by_username(username).get_json()
    settings = UserSetting(user_id=user.get('user_id'))
    db.session.add(settings)
    db.session.commit()
    return jsonify(user), 201

def login():
    data = request.get_json()
    user = get_user_by_username(data.get('username')).get_json()
    authenticated = bcrypt.checkpw(data.get('password').encode('utf-8'), user.get('password').encode('utf-8'))
    if not authenticated:
        return jsonify({'error': 'Incorrect credentials'}), 403
    token = create_token(user.get('user_id'))
    return jsonify({'authenticated': authenticated, 'token': token.token, 'id': user.get('user_id'), 'userEmail': user.get('email')}), 200

def logout():
    data = request.get_json()
    token = Token.query.filter_by(token = data.get('token')).first()
    db.session.delete(token)
    db.session.commit()
    token = token.__dict__
    token.pop('_sa_instance_state', None)
    return jsonify(token)

def create_token(id):
    token = uuid4()
    if not id or not token:
        return jsonify({'message': 'Missing parameters'})
    newToken = Token(user_id=id, token=token)
    db.session.add(newToken)
    db.session.commit()
    return newToken

def update_user_details(id):
    data = request.get_json()
    user = db.session.get(User, id)
    user.username = data.get('username')
    user.email = data.get('email')
    db.session.commit()
    return jsonify({'message': 'User details updated'})

def update_user_password(id):
    data = request.get_json()
    user = User.query.filter_by(user_id = id).first()
    password = user.__dict__.get('password')
    authenticated = bcrypt.checkpw(data.get('currentPassword').encode('utf-8'), password.encode('utf-8'))
    if not authenticated:
        return jsonify({'error': 'Incorrect credentials'}), 403
    newPassword = data.get('newPassword').encode('utf-8')
    salt = bcrypt.gensalt(rounds=int(os.getenv("SALT_ROUNDS")))
    hashed_password = bcrypt.hashpw(newPassword, salt).decode('utf-8')
    user.password = hashed_password
    db.session.commit()
    return jsonify({'message': 'Password updated'})

def check_password(id):
    data = request.get_json()
    user = db.session.get(User, id).__dict__
    authenticated = bcrypt.checkpw(data.get('password').encode('utf-8'), user.get('password').encode('utf-8'))
    # list = [authenticated]
    return jsonify({'status': authenticated})
