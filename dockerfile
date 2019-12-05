FROM ubuntu:16.04

MAINTAINER Vincenzo Norman Vitale

RUN apt-get update

RUN apt-get install -y python3 python3-pip

RUN mkdir /app

ADD tornado_hello_word /app

RUN pip3 install -r /app/requirements.txt

RUN chmod +x /app/main.py

WORKDIR /app

CMD ["python3","/app/main.py"]