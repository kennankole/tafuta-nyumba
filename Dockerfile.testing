FROM python:3.9.5-slim-buster 

WORKDIR /usr/src/ussd_app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHNOUNBUFFERED 1

RUN apt-get update && apt-get install -y netcat --no-install-recommends \
    && rm -rf  /var/lib/apt/lists/* 

RUN pip install --upgrade pip && pip install pipenv
COPY ./Pipfile* /usr/src/ussd_app/

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --system --deploy

COPY . /usr/src/ussd_app/

ENTRYPOINT [ "/usr/src/ussd_app/entrypoint.sh" ]