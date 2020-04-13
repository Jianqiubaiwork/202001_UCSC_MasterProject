#!/bin/sh

# verify that Postgres is healthy 
# before applying the migrations 
# and running the Django development server

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input --clear

# python manage.py createsuperuser --username "$SUPERUSER_USERNAME" --email "$SUPERUSER_EMAIL" --noinput
exec "$@"