from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)



# app.config.from_pyfile('settings.py')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nmtpqjvn:cbsEDgvmrjI52_hpEb7hkSsdxjYSgEDs@horton.db.elephantsql.com/nmtpqjvn'
#the following line's value can be anything, it's just a password of your choice
app.config['SECRET_KEY'] = '0e82eec5faf1fb25c1143590575f7a60'

db = SQLAlchemy(app)
