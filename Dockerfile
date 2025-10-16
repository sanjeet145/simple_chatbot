FROM python:3.11-slim

WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn", "server:app", "--bind", "0.0.0.0:8000", "--workers", "4"]
