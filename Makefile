
.PHONY: superuser
superuser:
	DJANGO_SUPERUSER_USERNAME=admin \
	DJANGO_SUPERUSER_PASSWORD=admin \
	DJANGO_SUPERUSER_EMAIL="admin@admin.com" \
	python manage.py createsuperuser --noinput

.PHONY: demo-app
demo-app:
	python manage.py migrate
	make superuser
	python manage.py runserver