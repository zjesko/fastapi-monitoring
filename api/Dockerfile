FROM python:3.8
WORKDIR /api

# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /api
