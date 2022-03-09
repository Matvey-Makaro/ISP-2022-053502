FROM python:3.10.2-alpine

WORKDIR /app

COPY . .

CMD ["python3", "main.py"]