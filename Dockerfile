FROM ubuntu


WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install pipenv
COPY Pipfile* /