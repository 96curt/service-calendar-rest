# Production Gunicorn Container
# https://dzone.com/articles/how-to-deploy-a-django-application-with-docker


FROM python:3.10.7
LABEL MAINTAINER="96curt"

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./prod/prod-settings.py ./web/settings.py
EXPOSE 8000
ENTRYPOINT [ "sh","./prod/entrypoint.sh" ]
