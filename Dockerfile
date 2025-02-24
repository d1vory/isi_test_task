FROM python:3.12

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Ensure the SQLite database is restored
RUN mkdir -p /app/data
COPY db_dump.sql /app/data/db_dump.sql

# Expose port for Django
EXPOSE 8000

CMD ["sh", "-c", "[ ! -f /app/data/db.sqlite3 ] && sqlite3 /app/data/db.sqlite3 < /app/data/db_dump.sql; python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
