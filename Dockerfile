# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py .
COPY config.json .

# Install system dependencies (timezone support)
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir requests

# Run application
CMD ["python", "app.py"]
