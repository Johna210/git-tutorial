FROM python:3.14.0a6-alpine3.21

RUN mkdir [DIRECTORY]

WORKDIR /[DIRECTORY]

COPY . .

CMD ["python3", "fizz_buzz.py"]
