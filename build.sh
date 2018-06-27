
cd personalPages && python3 compile_assets.py && cd ..

echo "yes" | python3 manage.py collectstatic


