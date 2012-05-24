Django-Bootstrap-Template
=========================

A starting point for Django projects that utilize Bootstrap. Also incorporates some best practices concerning project structure, settings.py etc. A work in progress. Inspired by:

- `Repository Structure and Python <http://www.kennethreitz.com/repository-structure-and-python.html>`_ by Kenneth Reitz
- `Django Best Practices <http://lincolnloop.com/django-best-practices/>`_

Why?
----

I start a lot of Django projects with Boostrap and found myself repeating the same operations to get the project set up and structured the way I want. The goal here is to set up a project the way I want once and use this as a starting point for future Django projects.

Getting Started
---------------

::

  virtualenv --no-site-packages venv
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py runserver

What's There
------------

- separate development and production settings
- static folder with Bootstrap css & js
- base.html set up with Bootstrap
- an app set up with a single view and it's own URLconf