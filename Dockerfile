#FROM jlesage/firefox
FROM python:alpine

WORKDIR /tmp

RUN apk add wget
RUN apk add firefox
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-linux64.tar.gz
RUN tar -xvf geckodriver-v0.29.1-linux64.tar.gz
RUN cp -rp geckodriver /usr/local/bin/geckodriver
RUN pip install selenium
RUN pip install pytest

