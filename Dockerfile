FROM ubuntu:22.04

RUN apt update && \ apt-get install enum4linux \ 
    && pip install --no-cache-dir -r requirements.txt \
    pip3 install customtkinter
WORKDIR /PROJECTE

ENV LANG es.utf8