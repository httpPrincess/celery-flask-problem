from flask import Flask
from celery import Celery

flask_app = Flask(__name__)
flask_app.config.update(
  CELERY_BROKER_URL='',
  CELERY_RESULT_BACKEND=''
  )

celery = Celery('example.task')
celery.conf.update(flask_app.config)


@celery.task
def my_celery_task(par):
  print 'Starting clery task %s' %par
  

@flask_app.route('/', methods=['GET'])
def starting_page():
  print 'GET on starting page'
  return 'Ok'


if __name__=="__main__":
  flask_app.run(debug=True)

