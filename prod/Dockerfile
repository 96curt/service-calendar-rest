# Production Container
# https://dzone.com/articles/how-to-deploy-a-django-application-with-docker


FROM python:3.10.7
LABEL MAINTAINER="96curt"

ENV PYTHONUNBUFFERED 1

COPY ./ usr/src/app
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENTRYPOINT [ "sh","./prod/entrypoint.sh" ]
