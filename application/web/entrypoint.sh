#!/bin/sh
# if [ "$DATABASE" = "postgres" ]
# then 
#     echo "Waiting for postgres..."

#     while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
#         sleep 0.1 
#     done

#     echo "PostgreSQL started"

# fi

# if [ "$FLASK_ENV" = "development" ]
# then 
#     echo "Creating the database tables..."
#     python manage.py create_db
#     echo "Tables created"

# fi

# exec "$@"

# gunicorn --bind 0.0.0.0:5000 application.web.app.manage:app
# gunicorn app.manage:app -w 2 --threads 2 -b 0.0.0.0:"$PORT"

gunicorn --bind 0.0.0.0:"$PORT" manage:app # Deployed to heroku