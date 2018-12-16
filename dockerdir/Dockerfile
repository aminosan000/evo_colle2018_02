FROM python:3.6-slim
MAINTAINER "Type your name."
RUN mkdir /var/www
RUN pip install Flask
COPY templates /var/www/templates
COPY app.py /var/www
WORKDIR /var/www
CMD python app.py
