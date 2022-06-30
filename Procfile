release: python manage.py migrate
web: gunicorn config.wsgi --log-file -
celery: celery -A config worker -l info --pool=solo
celerybeat: celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
celeryworker: celery -A config worker & celery -A config beat --pool=solo -l INFO & wait -n