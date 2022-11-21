FROM python:3.10
MAINTAINER "Luca Giulianini"
WORKDIR /app
COPY . /app
RUN pip install flask
RUN pip install pymongo
RUN pip install python-dotenv # Load environment variables from file
ENV FLASK_APP "app"
WORKDIR /app/restapi
# Run on port 80
ENTRYPOINT flask run --host=0.0.0.0 --port=80
