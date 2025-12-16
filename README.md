# Forest Resource Management System

Welcome to the Forest Resource Management System - a comprehensive solution for tracking, managing, and conserving the precious natural resources of our forests. This platform is designed to support forest managers, leaders, and scientists in monitoring the growth of flora and fauna, as well as the activities related to forest exploitation.

1. Installation Steps :
- Clone this repository, you should use a virtual environment to store your Django project’s
```shell
git clone https://github.com/hoangtung719/Forest-management-website.git
cd Forest-management-website
```
- Install the Django code with Pip:
```shell
python -m pip install Django
```
- Install other dependencies:
```shell
pip install dj-database-url gunicorn whitenoise requests
```
2. Run project:
- Make migrations:
```shell
python manage.py makemigrations <app_name>
```
- Migrate:
```shell
python manage.py migrate
```
- Create a superuser (Admin account):
```shell
python manage.py createsuperuser
```
- Run Server (Deploy):
```shell
python manage.py runserver
```

# Verification Walkthrough - Core Upgrade & Security

I have completed Phase 1 of the upgrade, focusing on infrastructure and Django 5.0 compatibility. Here is how to verify the changes.

## 1. Environment Setup Verification
Verify that the new infrastructure files are in place.

```bash
ls -l requirements.txt Dockerfile docker-compose.yml .env
```
Ensure [.env](file:///home/admin1/Projects/Forest-management-website/.env) contains the necessary variables (SECRET_KEY, DEBUG, DATABASE_URL).

## 2. Docker Build & Run (Requires Docker)
Since the system now depends on PostGIS and system-level GeoDjango dependencies (GDAL), the recommended way to run is via Docker.

```bash
# Build the images
docker-compose build

# Start the services
docker-compose up -d
```

## 3. Post-Deployment Verification
Once the container is running, execute the following to verify the Django version and database connection:

```bash
# Enter the web container
docker-compose exec web bash

# Check Django Version
python -c "import django; print(django.get_version())"
# Expected: 5.0+

# Run System Checks
python manage.py check
```

## 4. Code Compatibility Fixes Verified
I have proactively patched the following legacy issues to match Django 5.0 standards:

1.  **Authentication Backend**: Updated [App/EmailBackEnd.py](file:///home/admin1/Projects/Forest-management-website/App/EmailBackEnd.py) to accept receiving the `request` object.
2.  **Views**: Updated [App/views.py](file:///home/admin1/Projects/Forest-management-website/App/views.py) to use `django.contrib.auth.authenticate` instead of a direct class method call.
3.  **Models**: Fixed a crash in [App/models.py](file:///home/admin1/Projects/Forest-management-website/App/models.py) where creating a staff user relied on a hardcoded "Unit ID 1" that wouldn't exist in a fresh PostGIS database.

## 5. Next Steps
-   **Database Migration**: The system is configured to use Postgres. Run `python manage.py migrate` inside the container to create the schema.
-   **Superuser**: Create a new admin via `python manage.py createsuperuser`.
