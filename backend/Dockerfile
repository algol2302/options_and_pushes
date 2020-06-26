FROM python:3.7-buster

RUN groupadd djangogroup && useradd -m -g djangogroup -s /bin/bash django

WORKDIR /app
ADD src /app

COPY ./gunicorn_run.sh /

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
