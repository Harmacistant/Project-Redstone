FROM python:3

RUN apt-get update -y
WORKDIR /usr/src/web
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD bash