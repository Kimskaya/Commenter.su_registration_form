FROM python:3.11.4-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV WORK_DIR "/application/src"

WORKDIR ${WORK_DIR}

RUN apt update &&\
    apt install -y gcc &&\
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -U pip &&\
    pip install --no-cache-dir poetry &&\
    poetry config virtualenvs.create false

COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install --no-interaction
RUN playwright install

COPY . ${WORK_DIR}

ARG SIGN_IN_EMAIL
ENV SIGN_IN_EMAIL ${SIGN_IN_EMAIL}

ARG SIGN_IN_PASSWORD
ENV SIGN_IN_PASSWORD ${SIGN_IN_PASSWORD}

ENTRYPOINT ["/application/src/docker-entrypoint.sh"]
