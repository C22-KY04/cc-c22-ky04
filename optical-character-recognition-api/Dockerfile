# syntax=docker/dockerfile:1

FROM python:latest

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]