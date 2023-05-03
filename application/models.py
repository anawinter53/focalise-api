from application import app, db

app.app_context().push()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password
