FROM python:3.11-slim

WORKDIR /app

COPY python-app/ .

RUN pip install flask

CMD ["python", "web_calculator.py"]

