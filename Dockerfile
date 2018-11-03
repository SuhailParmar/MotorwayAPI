# Lightweight Python Image
FROM python:3.6-alpine

# Ability to use psql
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN mkdir /app
COPY requirements.txt /app

RUN pip install -r /app/requirements.txt
RUN rm /app/requirements.txt

ENV PYTHONUNBUFFERED 1