from flask import Flask
#requires newest version of sqlalchemy:
#pip install https://github.com/mitsuhiko/flask-sqlalchemy/archive/master.zip

from celery import Celery
from sqlalchemy import event
from sqlalchemy.orm.session import Session

flask_app = Flask(__name__)
flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@event.listens_for(Session, 'after_attach')
def my_attachement(session, intances):
  if not hasattr(session, '_model_changes'):
    session._model_changes = {}


from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(flask_app)  

from app import views
from app import models




