django_polls
============

.. toctree::
   :hidden:
   :maxdepth: 1

   license

.. contents:: Table of Contents
   :local:
   :backlinks: top
   :depth: 2

A basic poll application using the Django web framework

Features
--------

 * Application

   * Create, edit, and delete polls
   * Admin management of users and polls
   * User registration with email verification & social(GitHub) login
   * Bootstrap4 & crispy-forms decorations
   * Customizable user profile pages with bio, profile pic, & country flags
 * Dev/testing

   * basic module testing templates
   * Coverage reports
   * Debug-toolbar available
   * Examples of using Factories & pytest fixtures in account app testing
   * `shell_plus` with IPython via `django-extensions` package
   * Nox testing sessions for latest Python 3.9, 3.10, and 3.11

     * black
     * Sphinx documentaion generation
     * linting
       
       * flake8
       * flake8-bugbear
       * flake8-docstrings
       * flake8-import-order
       * safety(python package vulnerability testing)
     * pytest sessions with coverage


Installation
------------

To install the django_polls project,
run this command in your terminal:

.. code-block:: console

   $ git clone https://github.com/kevinbowen777/django_polls.git
   $ cd django_polls

Local installation
------------------

.. code-block:: console

   $ poetry shell
   $ poetry install
   $ python manage.py migrate
   $ python manage.py createsuperuser


Docker installation
-------------------

.. code-block:: console

   $ docker-compose up --build
   $ docker-compose python manage.py migrate
   $ docker-compose python manage.py createsuperuser


Usage
-----

To run django_polls, locally, enter the following on the command line:

.. code-block:: console

   $ python manage.py runserver

For both local, or Docker installations, browse to `<http://127.0.0.1:8000>`_ or `<http://127.0.0.1:8000/admin/>`_

Testing
-------

.. code-block:: console

   $ python manage.py runserver
   $ docker-compose exec web python manage.py test
   $ coverage run -m pytest
   $ nox --list-sessions
   $ nox
   $ nox -rs lint-3.11
   $ nox -s tests

Application Demo
----------------
Live demonstration of application running on Heroku:

`kbowen-django_polls <https://kbowen-django-polls.herokuapp.com/>`_

Reporting Bugs
--------------

Visit the django_polls `Issues page <https://github.com/kevinbowen777/django_polls/issues>`_ on GitHub.
