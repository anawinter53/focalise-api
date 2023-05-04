from application import app, db
from datetime import datetime

app.app_context().push()

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(30), nullable=False)
    
    setting = db.relationship('UserSetting', back_populates='user')
    task = db.relationship('Task', back_populates='user')
    message = db.relationship('Message', back_populates='user')
    token = db.relationship('Token', back_populates='user')

    def __init__(self, username, email, password):
        self.email = email
        self.password = password
        self.username = username        

class UserSetting(db.Model):
    __tablename__ = 'setting'
    setting_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    colour_scheme = db.Column(db.Integer, nullable=False, default=2)
    push_notifications = db.Column(db.Integer, nullable=False, default=2)
    points = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('User', back_populates='setting')

    def __init__(self, user_id, colour_scheme=2, push_notifications=2, points=0):
        self.user_id = user_id
        self.colour_scheme = colour_scheme
        self.push_notifications = push_notifications
        self.points = points

class Task(db.Model):
    __tablename__ = 'task'
    task_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    category_name = db.Column(db.String(30), nullable=False, default='Uncategorised')
    task_name = db.Column(db.String(30), nullable=False)
    task_url = db.Column(db.String(300), default='None')
    task_desc = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', back_populates='task')

    def __init__(self, user_id, category_name, task_name, task_url, task_desc):
        self.user_id = user_id
        self.category_name = category_name
        self.task_name = task_name
        self.task_url = task_url
        self.task_desc = task_desc
    
class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.String(200), nullable=False)

    user = db.relationship('User', back_populates='message')

    def __init__(self, user_id, date, content):
        self.user_id = user_id
        self.date = date
        self.content = content

class Token(db.Model):
    __tablename__ = 'token'
    token_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    token = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', back_populates='token')

    def __init__(self, user_id, token):
        self.user_id = user_id
        self.token = token

class Sensory(db.Model):
    __tablename__ = 'sensory'
    sensory_id = db.Column(db.Integer, primary_key=True)
    video_category = db.Column(db.String(100), nullable=False)
    video_url = db.Column(db.String(1000), nullable=False)

    def __init__(self, sensory_id, video_category, video_url):
        self.sensory_id = sensory_id
        self.video_category = video_category
        self.video_url = video_url




