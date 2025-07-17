FROM python:3.13-slim

ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y curl build-essential libpq-dev postgresql-client netcat-openbsd \
    && apt-get clean


RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* wait-for-postgres.sh /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

RUN chmod +x wait-for-postgres.sh

EXPOSE 8000

CMD ["./wait-for-postgres.sh", "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

