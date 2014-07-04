BROKER_URL='sqla+sqlite:///celerydb.sqlite'
#BROKER_URL = 'amqp://'
#result backed is not necessary and it is an additional overhead
#CELERY_RESULT_BACKEND='db+sqlite:///results.sqlite',
#CELERY_RESULT_SERIALIZER = 'json'

CELERY_RESULT_ENGINE_OPTIONS = {'echo': True}
#CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']