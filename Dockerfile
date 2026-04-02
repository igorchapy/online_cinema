FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=off

RUN apt update && apt install -y \
    dos2unix \
    && apt clean

RUN python -m pip install --upgrade pip && \
    pip install poetry

COPY ./poetry.lock /usr/src/poetry/poetry.lock
COPY ./pyproject.toml /usr/src/poetry/pyproject.toml

RUN poetry config virtualenvs.create false

WORKDIR /usr/src/poetry

RUN poetry lock
RUN poetry install --no-root --only main

WORKDIR /usr/src/fastapi

COPY ./src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
