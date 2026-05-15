# ── Stage 1: base image ────────────────────────────────────────────────────────
FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies required for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project source code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Expose Django development / Gunicorn port
EXPOSE 8000

# Entrypoint: run migrations then start Gunicorn
CMD ["sh", "-c", "python manage.py migrate && gunicorn students.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120"]