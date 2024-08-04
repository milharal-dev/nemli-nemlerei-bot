FROM python:3.12.4-slim-bookworm

WORKDIR /app

COPY pdm.lock pyproject.toml /app/

RUN pip install pdm && \
    pdm use 3.12.4 && \
    pdm install --no-self

ADD README.md /app/

COPY nemli /app/nemli

RUN pdm install --no-editable

CMD ["pdm", "run", "nemli"]
