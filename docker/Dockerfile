FROM python:3.12-slim

RUN apt-get update -y && \
    apt-get install -y libpq-dev build-essential && \
    pip3 install --upgrade pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt --no-cache-dir

COPY . /app
