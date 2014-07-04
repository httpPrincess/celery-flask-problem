from celery import Celery

celery = Celery(__name__)
celery.config_from_object('celeryconfig')


@celery.task(name='step1')
def step1(context):
  update_info(context, 'step1')
  context['pid'] = '991'
  return context

@celery.task(name='step2')
def step2(context):
  update_info(context, 'step2')
  context['location'] = 'httap'
  return context


def run_workflow(param):
  chain = step1.s(param) | step2.s()
  chain.apply_async()

def update_info(context, info):
  print 'Updating info for %s --> %s' % (context['id'], info)
