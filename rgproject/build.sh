#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Install PostgreSQL adapter
pip install psycopg2-binary dj-database-url

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
