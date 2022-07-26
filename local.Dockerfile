FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    gcc \
    libmariadb-dev-compat \
    libpq-dev \
    make

WORKDIR /app

COPY ./makefile makefile
COPY ./requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN make install
