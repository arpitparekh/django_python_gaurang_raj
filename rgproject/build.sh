#!/usr/bin/env bash
# exit on error
set -o errexit

# Print current directory and list files for debugging
echo "Current directory: $(pwd)"
ls -la

# Install dependencies
pip install -r requirements.txt

# Make sure Python can find the modules
export PYTHONPATH=$(pwd)

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate
