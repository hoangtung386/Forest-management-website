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
