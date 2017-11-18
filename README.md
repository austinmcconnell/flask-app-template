cookiecutter-flask
==================

A Flask template for [cookiecutter].

![Build Status]

Use it now
----------

    $ pip install cookiecutter
    $ cookiecutter https://github.com/austinmcconnell/cookiecutter-flask.git

You will be asked about your basic info (name, project name, app name,
etc.). This info will be used in your new project.

Features
--------

-   Bootstrap 3 and Font Awesome 4 with starter templates
-   Flask-SQLAlchemy with basic User model
-   Easy database migrations with Flask-Migrate
-   Flask-WTForms with login and registration forms
-   Flask-Login for authentication
-   Flask-Bcrypt for password hashing
-   Procfile for deploying to a PaaS (e.g. Heroku)
-   pytest and Factory-Boy for testing (example tests included)
-   Flask\'s Click CLI configured with simple commands
-   CSS and JS minification using webpack
-   npm support for frontend package management
-   Caching using Flask-Cache
-   Useful debug toolbar
-   Utilizes best practices: [Blueprints] and [Application Factory]
    patterns

Screenshots
-----------

[![Home page]][Home page]

[![Registration form]][Registration form]

Inspiration
-----------

-   [Building Websites in Python with Flask]
-   [Getting Bigger with Flask]
-   [Structuring Flask Apps]
-   [Flask-Foundation] by [@JackStouffer]
-   [flask-bones] by [@cburmeister]
-   [flask-basic-registration] by [@mjhea0]
-   [Flask Official Documentation]

License
-------

BSD licensed.

  [cookiecutter]: https://github.com/audreyr/cookiecutter
  [Build Status]: https://travis-ci.org/austinmcconnell/cookiecutter-flask.svg
  [![Build Status]]: https://travis-ci.org/austinmcconnell/cookiecutter-flask
  [Blueprints]: http://flask.pocoo.org/docs/blueprints/
  [Application Factory]: http://flask.pocoo.org/docs/patterns/appfactories/
  [Home page]: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-01.png
  [Registration form]: https://dl.dropboxusercontent.com/u/1693233/github/cookiecutter-flask-02.png.png
  [Building Websites in Python with Flask]: http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/
  [Getting Bigger with Flask]: http://maximebf.com/blog/2012/11/getting-bigger-with-flask/
  [Structuring Flask Apps]: http://charlesleifer.com/blog/structuring-flask-apps-a-how-to-for-those-coming-from-django/
  [Flask-Foundation]: https://github.com/JackStouffer/Flask-Foundation
  [@JackStouffer]: https://github.com/JackStouffer
  [flask-bones]: https://github.com/cburmeister/flask-bones
  [@cburmeister]: https://github.com/cburmeister
  [flask-basic-registration]: https://github.com/mjhea0/flask-basic-registration
  [@mjhea0]: https://github.com/mjhea0
  [Flask Official Documentation]: http://flask.pocoo.org/docs/
  [@wroberts]: https://github.com/wroberts
