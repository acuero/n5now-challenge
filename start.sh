#!/bin/sh
# python manage.py collectstatic --no-input
#set -o errexit
# set -o pipefail
#set -o nounset

# Aplicación de migraciones
python /app/manage.py migrate --no-input

# Levantamos server de Django
python /app/manage.py runserver 0.0.0.0:8000