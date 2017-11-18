cookiecutter-flask
==================

A Flask template for [cookiecutter].

[![Travis][travis_logo]][travis_link]

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
-   Utilizes best practices: [blueprints] and [application_factory]
    patterns

License
-------

BSD licensed.

[cookiecutter]: https://github.com/audreyr/cookiecutter
[travis_logo]: https://travis-ci.org/austinmcconnell/cookiecutter-flask.svg
[travis_link]: https://travis-ci.org/austinmcconnell/cookiecutter-flask
[blueprints]: http://flask.pocoo.org/docs/blueprints/
[application_factory]: http://flask.pocoo.org/docs/patterns/appfactories/
