# Celery Woker

Try celery worker

## Start RabbitMQ

`docker run -d -p 5672:5672 rabbitmq`

## Start Celery Worker Server

`celery -A tasks worker --loglevel=info`

## Reference

https://docs.celeryproject.org/en/stable/

https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html#first-steps

## Next

https://docs.celeryproject.org/en/stable/getting-started/next-steps.html#next-steps

https://docs.celeryproject.org/en/stable/userguide/index.html#guide

## Troubleshooting

https://docs.celeryproject.org/en/stable/faq.html#faq