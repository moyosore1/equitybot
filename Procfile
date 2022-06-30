release: python manage.py migrate
web: gunicorn config.wsgi --log-file -
celery: celery -A config worker -l info --pool=solo
celerybeat: celery -A core config -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler