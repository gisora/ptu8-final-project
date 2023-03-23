# syntax=docker/dockerfile:1
FROM python:3.10.10-slim-bullseye

WORKDIR /app

COPY ./nsk-api .
COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--forwarded-allow-ips", "'*'"]