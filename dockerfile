# Usa una imagen base de Ubuntu
FROM ubuntu:latest



WORKDIR /app

COPY ./ /app

RUN apt-get update && \
    apt-get install -y python3 python3-pip

RUN pip install --no-cache-dir -r requirements.txt







