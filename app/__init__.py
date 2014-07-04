from flask import Flask
from tasks import run_workflow

flask_app = Flask(__name__)

@flask_app.route('/', methods=['POST'])
def starting_page():
  print 'Submitting a task'
  context = dict()
  context['id'] = 661
  run_workflow(context)
  return 'Ok'




