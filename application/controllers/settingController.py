from application import db
from application.models.models import UserSetting
from flask import request, jsonify, render_template, redirect, url_for

def show_settings(id):
    setting = db.session.get(UserSetting, id)
    return {
        "user_id": setting.user_id,
        "colour_scheme": setting.colour_scheme,
        "font_name": setting.font_name,
        "font_size": setting.font_size,
        "push_notifications": setting.push_notifications,
        "points": setting.points
    }

def update_settings(id):
    data = request.get_json()
    settings = db.session.get(UserSetting, id)
    settings.colour_scheme = data.get('colour_scheme')
    settings.font_name = data.get('font_name')
    settings.font_size = data.get('font_size')
    settings.push_notifications = data.get('push_notifications')
    settings.points += data.get('points')
    db.session.commit()
    return jsonify({'message': 'Settings updated'})
