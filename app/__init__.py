from flask import Flask
from tasks import run_workflow
from flask.ext.sqlalchemy import SQLAlchemy

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(flask_app)

from app import views
from app import models




