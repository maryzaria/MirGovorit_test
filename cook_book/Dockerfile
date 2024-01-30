FROM python:3.10-alpine3.16

COPY ./requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY . /src

WORKDIR /src