FROM python:3.11

WORKDIR /app
RUN apt-get update && apt-get install -y sqlite3

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/data

CMD ["sh", "-c", "if [ ! -f /app/db.sqlite3 ]; then sqlite3 /app/db.sqlite3 < /app/db_dump.sql; fi && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
