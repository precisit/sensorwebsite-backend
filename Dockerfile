FROM python:3.8-alpine

RUN adduser -D weather

WORKDIR /home/sensorwebsite

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY application.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP application.py

RUN chown -R weather ./
USER weather

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
