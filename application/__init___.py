from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expensesDB.db'
app.config['SECRET_KEY'] = '0e82eec5faf1fb25c1143590575f7a60'
db = SQLAlchemy(app)
