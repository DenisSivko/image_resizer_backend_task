#!/bin/sh
python manage.py migrate
python manage.py compilemessages
python manage.py collectstatic --noinput
exec "$@"