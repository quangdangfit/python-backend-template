# Restful API Template

## Installation Guide

### Clone from Git
* git clone git@gitlab.com:freelance_group/backend_template.git
* cd backend_template/
* \# git checkout develop|master
* git pull

### Make dir for logging
* sudo mkdir /var/log/backend_template
* sudo chown <user>. /var/log/backend_template

### Make dir for static files
* sudo mkdir -p /var/www/api/static
* sudo chown -R <user>. /var/www/api

### Make virtual env
* virtualenv -p /usr/bin/python3 .venv

### Setup
* Create env setting file: `cp .env.sample .env`
* Install require packages: `.venv/bin/pip install -r requirements.txt`
* Run migrate: `.venv/bin/python manage.py migrate`
* Publish assets: `.venv/bin/python manage.py collectstatic`
* Create superuser `.venv/bin/python manage.py createsuperuser --email admin@mail.vn --username admin`.
* Using `admin123` as password.

### Startup
* Run project on port **8080** : `.venv/bin/python manage.py runserver 0.0.0.0:8080`
* Access `http://localhost:8080` for testing.

## Install Rest Framework 

Base on `http://www.django-rest-framework.org/tutorial/quickstart/#project-setup`.

Access `curl -H 'Accept: application/json; indent=4' -u admin:admin123 http://127.0.0.1:8080/users/` for testing.

## Module structure
Each module is spitted by repository pattern
##### Repository Pattern
![alt text](https://imgur.com/VWxivOX.png "Repository Pattern")


##### Module api structure
* routers/: define api url, request body, params
* extensions/: setup base configuration
* helpers/: define helper function
* models/: define orm model  
* repositories/: define repository to access data  
* services/: handle business logic  
* admin/: define model admin views
* tests/: app test script

### 📙 Resource

#### Libraries
- Django https://www.djangoproject.com/ 
- Django Rest Framework: document api https://www.django-rest-framework.org/

### Contributing
If you want to contribute to this boilerplate, clone the repository and just start making pull requests.
