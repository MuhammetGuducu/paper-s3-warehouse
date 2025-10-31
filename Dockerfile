FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl netcat-openbsd postgresql-client && \
    rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY src/backend/requirements.txt ./requirements.txt
RUN uv pip install -r requirements.txt --system

COPY src/ .

EXPOSE 8000