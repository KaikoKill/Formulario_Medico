#!/bin/bash

# Instalar dependencias
pip install -r requirements.txt

# Colectar archivos estáticos
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput