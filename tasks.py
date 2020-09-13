from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://localhost')

app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y