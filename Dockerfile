FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y curl wget

RUN pip install -r requirements.txt
RUN pip install uvicorn

copy . .

ENV PYTHONPATH "${PYTHONPATH}:/app"
# RUN uvicorn service:app