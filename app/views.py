from app import flask_app
from flask import jsonify
from app import db
from models import Request
import json

@flask_app.route('/', methods=['POST'])
def starting_page():
  print 'Submitting a task'
  r = Request()
  r.name = 'Some random name'
  db.session.add(r)
  db.session.commit()
  
  context = dict()
  context['id'] = r.id
  db.session.close()
  run_workflow(context)
  return 'Ok', 201

@flask_app.route('/', methods=['GET'])
def get_all_requests():
  l = Request.query.all()
  return jsonify(requests=[i.serialize for i in l])

@flask_app.route('/<id>', methods=['GET'])
def get_single_request(id):
  r = Request.query.get_or_404(id)
  return jsonify(r.serialize), 200
 
  