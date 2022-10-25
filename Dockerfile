FROM python:3.10.7
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y default-mysql-client
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt