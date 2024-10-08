FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
