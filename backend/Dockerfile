# Dockerfile
FROM python:3.11

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app
COPY ./run.py /app/run.py
COPY ./config.py /app/config.py
WORKDIR /app


CMD ["python", "run.py"]