#!/bin/bash

ACCENT='\033[0;32m'
NC='\033[0m' # No Color

python3 manage.py makemigrations && python3 manage.py makemigrations personalPages && python3 manage.py migrate

if [ -n "$ADMIN_PASS" ];
	then
    # Setup admin account in database    
    echo "from django.contrib.auth.models import User; User.objects.filter(email='$ADMIN_EMAIL').delete(); User.objects.create_superuser('admin', '$ADMIN_EMAIL', '$ADMIN_PASS')" | python3 manage.py shell

    echo -e "${ACCENT}Web app admin account created ${NV}with username 'admin', login at <hostname>/admin"
fi

# Start Gunicorn processes
echo Starting Gunicorn on port 8000.
exec gunicorn PersonalWebsite.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3