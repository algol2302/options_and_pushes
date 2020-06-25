FROM python:3.6-buster

RUN groupadd djangogroup && useradd -m -g djangogroup -s /bin/bash django

WORKDIR /app
ADD src /app

COPY ./gunicorn_run.sh /

RUN pip install -r requirements.txt
