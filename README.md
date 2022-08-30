## django_polls 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django_polls.svg)](https://github.com/kevinbowen777/django_polls/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A basic poll application using the Django web framework

This repository contains a polling application demonstrating basic Django
functionality.

 - A public site that lets people view polls and vote in them.
 - An admin site for adding, changing, and deleting polls.
 - User sign up with email validation
 - 3rd party sign-in integration with GitHub

---
## Installation

 - `git clone git@github.com:kevinbowen777/django_polls.git`
 - `cd django_polls`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---

### Live Demo on Heroku:
 - [Polls app](https://kbowen-django-polls.herokuapp.com/)

### Screenshots
![Poll list](https://github.com/kevinbowen777/django_polls/blob/master/images/poll_list.png)

![Poll detail](https://github.com/kevinbowen777/django_polls/blob/master/images/poll_detail.png)


![Poll results](https://github.com/kevinbowen777/django_polls/blob/master/images/poll_results.png)

---
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/django_polls/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_polls/issues)
      to view currently open bug reports or open a new issue.
