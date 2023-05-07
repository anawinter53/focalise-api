from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
CORS(app)

# possibly set app.config to connect to test db if testing = True?
if app.config['TESTING'] == True: 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("TEST_DB_URL")
else: 
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
    
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

db = SQLAlchemy(app)

from application.routes import *
app.register_blueprint(user_routes, url_prefix="/users")
app.register_blueprint(task_routes, url_prefix="/tasks")
app.register_blueprint(sensory_routes, url_prefix="/sensory")
app.register_blueprint(setting_routes, url_prefix="/settings")
app.register_blueprint(message_routes, url_prefix="/messages")
