FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
# sqlite
RUN apt-get update
RUN apt-get install sqlite3 libsqlite3-dev -y


RUN pip install -r requirements.txt
ADD . /code/
RUN rm /code/*.env &
