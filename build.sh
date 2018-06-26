if [ -z ${ADMIN_PASS+x} ];
	then
	echo "Admin password cannot be empty, please set ADMIN_PASS environment variable."
	exit 1
fi

cd personalPages && python3 compile_assets.py && cd ..

echo "yes" | python3 manage.py collectstatic

python3 manage.py makemigrations && python3 manage.py makemigrations personalPages && python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.filter(email='$ADMIN_EMAIL').delete(); User.objects.create_superuser('admin', '$ADMIN_EMAIL', '$ADMIN_PASS')" | python3 manage.py shell

echo "Admin account created, with username: 'admin' and your supplied password in ADMIN_PASS"
