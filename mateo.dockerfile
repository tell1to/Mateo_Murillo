FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir pytest

EXPOSE 3000

CMD ["python", "main.py"]
