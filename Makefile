migrate:
	python manage.py makemigrations & python manage.py migrate

migrateEmployment:
	python manage.py makemigrations employment & python manage.py migrate employment --database=employment

run:
	python manage.py runserver

createsuperuser:
	python manage.py createsuperuser