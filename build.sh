
echo "BUILD START"
# Instalar dependencias
python3.9 -m pip install -r requirements.txt
# Recopilar archivos estáticos
python3.9 manage.py collectstatic --noinput


python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "BUILD END"