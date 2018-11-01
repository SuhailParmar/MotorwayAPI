# Lightweight Python Image
FROM python:3.6-alpine

RUN mkdir /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
RUN rm /app/requirements.txt

ENV PYTHONUNBUFFERED 1