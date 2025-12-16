# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Labels for GitHub Container Registry
LABEL org.opencontainers.image.source=https://github.com/hoangtung386/Forest-management-website
LABEL org.opencontainers.image.description="Forest Management System Container"
LABEL org.opencontainers.image.licenses=MIT

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for GeoDjango
# Combine apt-get update and install to pass the checks
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

# Install dependencies as root to avoid permission issues with system folders
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Change ownership of the application code to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Expose port
EXPOSE 8000
