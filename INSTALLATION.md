# Installation & Deployment Guide

## 🐳 Docker Deployment (Recommended)

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed

### Option 1: Pull from GitHub Container Registry (GHCR)

You can pull the pre-built image directly from our GitHub Container Registry.

```bash
# Pull the latest image
docker pull ghcr.io/hoangtung386/forest-management-website:latest

# Or pull a specific version
docker pull ghcr.io/hoangtung386/forest-management-website:v1.0.0
```

### Option 2: Build from Source

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/hoangtung386/Forest-management-website.git
    cd Forest-management-website
    ```

2.  **Create `.env` file**:
    Copy the example environment file and configure it (if applicable).
    ```bash
    cp .env.example .env
    ```

3.  **Build and Run with Docker Compose**:
    ```bash
    docker-compose up -d --build
    ```

4.  **Access the application**:
    Open your browser and navigate to `http://localhost:8000`.

---

## 🛠️ Manual Installation (Development)

### Prerequisites

- Python 3.12+
- PostgreSQL 15+
- GDAL/GEOS libraries (for PostGIS)

### Steps

1.  **Install System Dependencies (Ubuntu/Debian)**:
    ```bash
    sudo apt-get update
    sudo apt-get install binutils libproj-dev gdal-bin
    ```

2.  **Clone and Enter Directory**:
    ```bash
    git clone https://github.com/hoangtung386/Forest-management-website.git
    cd Forest-management-website
    ```

3.  **Create Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure Database**:
    Ensure PostgreSQL is running and create a database with PostGIS extension enabled.

6.  **Run Migrations**:
    ```bash
    python manage.py migrate
    ```

7.  **Create Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

8.  **Run Development Server**:
    ```bash
    python manage.py runserver
    ```

---

## 🔑 Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `DEBUG` | Enable debug mode | `False` |
| `SECRET_KEY` | Django secret key | `change-me` |
| `DB_NAME` | Database name | `forest_db` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | `postgres` |
| `DB_HOST` | Database host | `db` |
| `DB_PORT` | Database port | `5432` |
