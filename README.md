# Project: Quan ly tai nguyen rung
1. Installation Steps :
- Clone this repository, you should use a virtual environment to store your Django project’s
```shell
$ git clone https://github.com/Jackson2706/Quan_ly_tai_nguyen_rung.git
$ cd Quan_ly_tai_nguyen_rung
```
- Install the Django code with Pip:
```shell
$ python -m pip install Django
```
- Install other dependencies:
```shell
$ pip install dj-database-url gunicorn whitenoise requests
```
2. Run project:
- Make migrations:
```shell
$ python manage.py makemigrations <app_name>
```
- Migrate:
```shell
$ python manage.py migrate
```
- Create a superuser (Admin account):
```shell
$ python manage.py createsuperuser
```
- Run Server (Deploy):
```shell
$ python manage.py runserver
```
