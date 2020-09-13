# Celery Woker

Try celery worker

## Start RabbitMQ

`docker run -d -p 5672:5672 rabbitmq`

## Start Celery Worker Server

`celery -A tasks worker --loglevel=info`

## Reference

https://docs.celeryproject.org/en/stable/

https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps
