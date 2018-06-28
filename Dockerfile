FROM python:3
ARG SECRET_KEY
ARG ALLOWED_HOSTS_LIST

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN ./build.sh
