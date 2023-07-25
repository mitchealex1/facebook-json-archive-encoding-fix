ARG python_image_version=3.10

FROM python:${python_image_version}

ARG poetry_version=1.2.0

ENV POETRY_VERSION="${poetry_version}" \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE="false"
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 - 

WORKDIR /usr/facebook_json_archive_encoding_fix
COPY . .
RUN poetry install
WORKDIR /usr/facebook_json_archive_encoding_fix/src

ENTRYPOINT [ "poetry", "run", "python", "main.py" ]
CMD ["--help"]