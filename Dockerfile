FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "localhost", "--port", "8000"]