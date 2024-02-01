FROM python:3.10-alpine3.16

WORKDIR /src/

ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

COPY . .

ENTRYPOINT ["/src/entrypoint.sh"]