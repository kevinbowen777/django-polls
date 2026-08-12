.. _`changelog`:

=========
Changelog
=========

``django-polls`` issues are filed on `GitHub <https://github.com/kevinbowen777/django-polls/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

django-polls 0.3.5 (2026-08-12)
===============================

Improved documentation
----------------------

-  (`#603 <https://github.com/kevinbowen777/django-polls/603>`_): Add towncrier 25.8.0.


New features
------------

-  (`#627 <https://github.com/kevinbowen777/django-polls/627>`_): Upgrade to Django 6.0.8

django-polls 0.3.4 (2026-07-25)
===============================

Contributor-facing changes
--------------------------

-  (`#566 <https://github.com/kevinbowen777/django-polls/566>`_): Update Docker with Python 3.14 & Postgres 15.15.

-  (`#576 <https://github.com/kevinbowen777/django-polls/576>`_): Add Python 3.14 support.

-  (`#621 <https://github.com/kevinbowen777/django-polls/621>`_): Update with Python 3.14.6 & 3.13.14.

-  (`#623 <https://github.com/kevinbowen777/django-polls/623>`_): Rename default branch to main.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#617 <https://github.com/kevinbowen777/django-polls/617>`_): Drop support for Python 3.11.


New features
------------

-  (`#619 <https://github.com/kevinbowen777/django-polls/619>`_): Upgrade Django to 5.2.15.

django-polls 0.3.3 (2025-04-29)
===============================

Contributor-facing changes
--------------------------

-  (`#520 <https://github.com/kevinbowen777/django-polls/520>`_): Upgrade PostgreSQL to 15.11.

-  (`#530 <https://github.com/kevinbowen777/django-polls/530>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#526 <https://github.com/kevinbowen777/django-polls/526>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#525 <https://github.com/kevinbowen777/django-polls/525>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#468 <https://github.com/kevinbowen777/django-polls/468>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#531 <https://github.com/kevinbowen777/django-polls/531>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#534 <https://github.com/kevinbowen777/django-polls/534>`_): Replace safety package with pip-audit.

django-polls 0.3.2 (2025-01-10)
===============================

Contributor-facing changes
--------------------------

-  (`#460 <https://github.com/kevinbowen777/django-polls/460>`_): Upgrade to psycopg 3.

-  (`#465 <https://github.com/kevinbowen777/django-polls/465>`_): Add support for Python 3.13

-  (`#507 <https://github.com/kevinbowen777/django-polls/507>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#499 <https://github.com/kevinbowen777/django-polls/499>`_): Upgrade Django to 5.1.4

django-polls 0.3.0 (2023-12-21)
===============================

Contributor-facing changes
--------------------------

-  (`#200 <https://github.com/kevinbowen777/django-polls/200>`_): Migrate to non-root Docker user & venv.

-  (`#356 <https://github.com/kevinbowen777/django-polls/356>`_): Update Python to 3.12.0.

-  (`#370 <https://github.com/kevinbowen777/django-polls/370>`_): Upgrade Poetry to 1.7.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#362 <https://github.com/kevinbowen777/django-polls/362>`_): Drop support for Python 3.9.


Improved documentation
----------------------

-  (`#292 <https://github.com/kevinbowen777/django-polls/292>`_): Update Sphinx theme to Furo


New features
------------

-  (`#375 <https://github.com/kevinbowen777/django-polls/375>`_): Upgrade to Django 5.0.

django-polls 0.2.0 (2023-05-11)
===============================

Contributor-facing changes
--------------------------

-  (`#212 <https://github.com/kevinbowen777/django-polls/212>`_): Install ruff. Drop flake8-* packages.

django-polls 0.1.0 (2023-05-08)
===============================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#209 <https://github.com/kevinbowen777/django-polls/209>`_): Add support for Python 3.12.

-  (`#215 <https://github.com/kevinbowen777/django-polls/215>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#220 <https://github.com/kevinbowen777/django-polls/220>`_): Upgrade PostgreSQL to 15.2


Improved documentation
----------------------

-  (`#30 <https://github.com/kevinbowen777/django-polls/30>`_): Add Sphinx for documentation


New features
------------

-  (`#217 <https://github.com/kevinbowen777/django-polls/217>`_): Upgrade to Django 4.2.

django-polls 0.0.1 (2022-07-05)
===============================

Contributor-facing changes
--------------------------

-  (`#47 <https://github.com/kevinbowen777/django-polls/47>`_): Add support for Python 3.11


New features
------------

-  (`#45 <https://github.com/kevinbowen777/django-polls/45>`_): Support Django 4.0.6.

-  (`#52 <https://github.com/kevinbowen777/django-polls/52>`_): Build Docker support for Heroku deployment.


Miscellaneous internal changes
------------------------------

- : Initial commit
