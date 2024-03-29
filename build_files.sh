virtualenv env
env/Scripts/activate
pip install -r requirements.txt
python3.9 manage.py collectstatic
python manage.py migrate
python manage.py makemigrations