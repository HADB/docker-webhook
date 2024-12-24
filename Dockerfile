FROM python:3.13-alpine

RUN apk --no-cache --update add docker-cli docker-cli-compose
RUN pip install poetry==1.8.3

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1

WORKDIR /app

COPY pyproject.toml poetry.lock /app
RUN poetry install

COPY main.py .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"]
