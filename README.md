## django_polls

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django_polls.svg)](https://github.com/kevinbowen777/django_polls/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A basic poll application using the Django web framework

---

###Features

 - Application
     - A public site that lets people view polls and vote in them.
     - An admin site for adding, changing, and deleting polls.
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
     - image carousel
     - pagination template
 - Dev/testing
     - basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generations
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage

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
### Testing
 - `docker-compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.9, 3.10, 3.11
     - e.g. `nox`, `nox -rs lint-3.11`, `nox -s tests`

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
