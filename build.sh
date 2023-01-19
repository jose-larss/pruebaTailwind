#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py createsuperuser --username USERNAME --noinput
python manage.py collectstatic --no-input
python manage.py migrate