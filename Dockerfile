# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Add labels for GitHub Container Registry
LABEL org.opencontainers.image.source="https://github.com/hoangtung719/Forest-management-website"
LABEL org.opencontainers.image.description="Modern Forest Management System - A comprehensive platform for sustainable forestry"
LABEL org.opencontainers.image.licenses="MIT"
LABEL org.opencontainers.image.title="Forest Management System"
LABEL org.opencontainers.image.version="1.0.0"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for GeoDjango
RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    python3-gdal \
    && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd -m -s /bin/bash appuser

# Set work directory
WORKDIR /app

# Install Python dependencies as root
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000')"

# Default command
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "System.wsgi:application"]
