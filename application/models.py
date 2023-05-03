from application import app, db

app.app_context().push()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    settings = db.relationship('UserSettings', back_populates='user')
    tasks = db.relationship('Tasks', back_populates='user')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class UserSettings(db.Model):
    __tablename__ = 'settings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    colour_scheme = db.Column(db.Integer, nullable=False, default=2)
    push_notifications = db.Column(db.Integer, nullable=False, default=2)
    points = db.Column(db.Integer, nullable=False, default=0)

    user = db.relationship('Users', back_populates='settings')

    def __init__(self, user_id, colour_scheme, push_notifications, points):
        self.user_id = user_id
        self.colour_scheme = colour_scheme
        self.push_notifications = push_notifications
        self.points = points

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_name = db.Column(db.String(30), nullable=False, default='Uncategorised')
    task_name = db.Column(db.String(30), nullable=False)
    task_url = db.Column(db.String(300), default='None')
    task_desc = db.Column(db.String(100), nullable=False)

    user = db.relationship('Users', back_populates='tasks')

    def __init__(self, user_id, category_name, task_name, task_url, task_desc):
        self.user_id = user_id
        self.category_name = category_name
        self.task_name = task_name
        self.task_url = task_url
        self.task_desc = task_desc
    





