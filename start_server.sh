#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn on port 8000.
exec gunicorn PersonalWebsite.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 2