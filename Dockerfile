FROM python:3.10-slim

WORKDIR /input

COPY . /input/

CMD ["python", "input.py"]