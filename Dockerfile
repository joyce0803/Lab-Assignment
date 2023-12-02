FROM python:3.8.0

LABEL authors="joyce"



RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app



RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD python /app/model.py && python /app/server.py
