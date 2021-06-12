FROM python:3.8.5-alpine

WORKDIR /app

ADD ./web/ ./ 

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add mariadb-dev\
    && apk add jpeg-dev zlib-dev
    # && apk del build-deps

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install ipfshttpclient==0.8.0a1
