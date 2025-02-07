#!/bin/bash
# Instalar dependencias
pip install -r requirements.txt
# Recopilar archivos estáticos
python manage.py collectstatic --noinput
# Migrar la base de datos (si es necesario)
python manage.py makemigrations --noinput
python manage.py migrate --noinput