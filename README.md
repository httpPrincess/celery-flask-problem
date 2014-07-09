Celery-Flask Demo
====================

Small application written to investigate the problems occurring when using Celery in Flask when Celery is using SQLAlchemy as broker.

Problem
-------
Flask-SQLAlchemy is registering callbacks in SQLAlchemy.Session and it also decorates Session with additional field(s). If at the same
time normal SQLAlchemy.Session is used (for instance by Celery) problems occure: callbacks access fields that don't exist in pure Session.

Towards solution
----------------
For the application it is possible to fix the problem in a programmatic way by adding a callback that is called before Flask-SQLAlchemy
callbacks are called:

    @event.listens_for(Session, 'after_attach')
    def my_attachement(session, intances):
     if not hasattr(session, '_model_changes'):
       session._model_changes = {}


Unfortunately the same problem occurs while starting the workers

    ./start_worker.sh
   

Here (due to high parallelization) the registration of additional callback does not seem to work. 


Solution
--------

The development version of the Flask-SQLAlchemy contains improved version of callbacks that check if the Session is instance of Flask-SQLAlchemy decorated 
session. The installation is possible through:

    pip install https://github.com/mitsuhiko/flask-sqlalchemy/archive/master.zip
   
