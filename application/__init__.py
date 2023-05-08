from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()

def create_app(env=None):
    app = Flask(__name__)

    if env == 'TEST':
        app.config['TESTING'] == True
        app.config["DEBUG"] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("TEST_DB_URL")
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        url = os.getenv("TEST_DB_URL")
        if 'postgresql' not in url:
            url.replace("postgres","postgresql")
        

    else:
        app.config["TESTING"] = False
        app.config["DEBUG"] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
        app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
        url = os.getenv("DB_URL")
        if 'postgresql' not in url:
            url.replace("postgres","postgresql")   
           

    from application.models.models import db
    db.init_app(app)


    CORS(app)

    from application.routes import user_routes, task_routes, message_routes, sensory_routes, setting_routes
    app.register_blueprint(user_routes, url_prefix="/users")
    app.register_blueprint(task_routes, url_prefix="/tasks")
    app.register_blueprint(sensory_routes, url_prefix="/sensory")
    app.register_blueprint(setting_routes, url_prefix="/settings")
    app.register_blueprint(message_routes, url_prefix="/messages")
        
    return app
