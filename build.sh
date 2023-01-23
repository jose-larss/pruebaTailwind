#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py createsuperuser --no-input
#python manage.py createsuperuser --username admin 
python manage.py collectstatic --no-input
python manage.py migrate 

#python manage.py loaddata prueba.json

python manage.py tailwind build 