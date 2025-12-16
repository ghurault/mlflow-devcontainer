ARG PYTHON_VERSION=3.12

FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION}-bookworm

COPY requirements.txt /tmp/pip-tmp/
RUN pip install --upgrade pip && \
    pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt && \
    rm -rf /tmp/pip-tmp
