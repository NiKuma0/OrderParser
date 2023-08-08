#!/usr/bin/sh

/usr/bin/env python ./orderparser/manage.py migrate
/usr/bin/env python ./orderparser/manage.py createsuperuser --noinput --skip-checks

/usr/bin/env python -m gunicorn orderparser.core.wsgi:application -c ./gunicorn.conf.py
