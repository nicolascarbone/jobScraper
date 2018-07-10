
FROM python:3.6

MAINTAINER Nicolas Carbone "carbone.nicolas.ariel@gmail.com"

ENV REDIS_HOST redis
ENV REDIS_PORT 6379

RUN mkdir -p /var/www/simplify/
COPY requirements.txt /var/www/simplify/

RUN pip install -r /var/www/simplify/requirements.txt
COPY . /var/www/simplify
WORKDIR /var/www/simplify/
RUN find . -path "**/*.pyc"  -delete