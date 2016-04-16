 rm -rvf __pycache__/ db.sqlite3 */__pycache__ */migrations 


python manage.py migrate &&  python manage.py createsuperuser --email fx@microcheap.info && python manage.py makemigrations contact  && python manage.py migrate contact && python populate_for_test.py

