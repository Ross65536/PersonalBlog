FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/

# sqlite
RUN apt-get update && apt-get install sqlite3 libsqlite3-dev -y
RUN /usr/bin/sqlite3 /code/db.db

# RUN cd /code/personalPages && python3 compile_assets.py && cd ..
# RUN python3 manage.py makemigrations && python3 manage.py makemigrations personalPages && python3 manage.py migrate

RUN ls /code/personalPages/static/personalPages/css/