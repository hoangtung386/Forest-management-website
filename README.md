# 🌲 Modern Forest Management System (FMS)

> **A Next-Generation Platform for Sustainable Forestry & Biodiversity Conservation**

[![Django 5.0](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django)](https://docs.djangoproject.com/en/5.0/)
[![PostGIS](https://img.shields.io/badge/PostGIS-Enabled-336791?style=for-the-badge&logo=postgresql)](https://postgis.net/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker)](https://www.docker.com/)

## 📖 Overview

The **Modern Forest Management System (FMS)** is a comprehensive digital solution designed to empower forest rangers, scientists, and administrators. It transforms traditional forestry management into a data-driven discipline, integrating **Geographic Information Systems (GIS)**, **Real-time Monitoring**, and **AI-powered Biodiversity Tracking**.

### 🚀 Key Capabilities
*   **Resource Tracking**: Manage detailed records of tree species, seed sources, and wood processing facilities.
*   **Biodiversity Protection**: Monitor endangered flora and fauna with precise location data.
*   **GIS Integration**: Visualize forest boundaries, patrol routes, and incident hotspots on interactive maps (PostGIS enabled).
*   **Operational Efficiency**: Streamline reporting between field units and central administration.

---

## 🛠️ Technology Stack

This project has been modernized to meets the standards of high-performance enterprise applications:

*   **Backend Core**: Django 5.0 (Python 3.12)
*   **Database**: PostgreSQL 15 + PostGIS (Spatial Database)
*   **Containerization**: Docker & Docker Compose
*   **Frontend**: AdminLTE 3 (Hybrid Architecture)
*   **API**: Django REST Framework (Infrastructure Ready)

---

## ⚡ Quick Start (Docker)

The recommended way to deploy FMS is via Docker, which handles all complex spatial dependencies (GDAL/GEOS) automatically.

### Prerequisites
*   [Docker Desktop](https://www.docker.com/products/docker-desktop) or Docker Engine
*   Git

### Installation

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/hoangtung719/Forest-management-website.git
    cd Forest-management-website
    ```

2.  **Configure Environment**
    Ensure a `.env` file exists in the root directory. You can copy the example:
    ```bash
    cp .env.example .env
    # Edit .env variables as needed (e.g., SECRET_KEY, DEBUG)
    ```

3.  **Build & Launch**
    ```bash
    docker compose up -d --build
    ```

4.  **Initialize Database**
    Run migrations to set up the spatial database schema:
    ```bash
    docker compose exec web python manage.py migrate
    ```

5.  **Create Administrator**
    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

6.  **Access the Dashboard**
    Open your browser to: [http://localhost:8000](http://localhost:8000)

---

## 🗺️ Roadmap & Modernization Plan

We are actively upgrading this legacy system into a state-of-the-art platform:

- [x] **Phase 1: Infrastructure Overhaul**
    - Containerization (Docker)
    - Migration to PostgreSQL/PostGIS
    - Django 5.0 Upgrade
- [ ] **Phase 2: API-First Architecture**
    - RESTful API implementation
    - Mobile App Backend readiness
- [ ] **Phase 3: Advanced GIS**
    - Leaflet/Mapbox Integration
    - Heatmap visualization for deforestation/fire risks
- [ ] **Phase 4: AI & IoT**
    - Computer Vision for species identification
    - Real-time IoT sensor integration (Humidity, Temperature)

---

## 🤝 Contribution

Contributions are welcome! Please examine the `task.md` file in the artifacts directory for current priorities.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

*Built with ❤️ for the Forest.*
