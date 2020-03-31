FROM python:3.8.1-alpine3.11

RUN apk add --no-cache gcc musl-dev make libffi libffi-dev

WORKDIR /usr/src/app

COPY . .
RUN pip install --quiet --upgrade pip && \
    pip install --quiet --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app:app", "--reload", "--port", "8000", "--host", "0.0.0.0", "--workers", "10", "--limit-concurrency", "100"]
