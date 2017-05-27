from flask import Flask
from app import views, models
from flasksqlalchemy import SQLAlchemy
import logging
import sys
app = Flask(__name__)


app.config['SECRET_KEY'] = "$$tarz"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

UPLOAD_FOLDER = './app/static/uploads'

db = SQLAlchemy(app)
 
app.config.from_object(__name__)


app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)



app.config.from_object(__name__)
from app import views, models