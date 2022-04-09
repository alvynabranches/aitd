FROM python:3.9

WORKDIR /app

COPY requirements.txt requirements.txt
COPY main.py main.py

RUN pip3 install -r requirements.txt

EXPOSE 8085
CMD python3 main.py