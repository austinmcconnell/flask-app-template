#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Invoke tasks."""
import os
import json
import shutil
import webbrowser

from invoke import task

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'cookiecutter.json'), 'r') as fp:
    COOKIECUTTER_SETTINGS = json.load(fp)
# Match default value of app_name from cookiecutter.json
APP_NAME = COOKIECUTTER_SETTINGS["app_name"]
COOKIE = os.path.join(HERE, APP_NAME)
AUTOAPP = os.path.join(COOKIE, 'autoapp.py')


def _run_npm_command(ctx, command):
    os.chdir(COOKIE)
    ctx.run('npm {0}'.format(command), echo=True)
    os.chdir(HERE)


@task
def build(ctx):
    """Build the cookiecutter."""
    ctx.run('cookiecutter {0} --no-input'.format(HERE))
    _run_npm_command(ctx, 'install')


@task
def clean(ctx):
    """Clean out generated cookiecutter."""
    if os.path.exists(COOKIE):
        shutil.rmtree(COOKIE)
        print('Removed {0}'.format(COOKIE))
    else:
        print('App directory does not exist. Skipping.')


def _run_flask_command(ctx, command):
    ctx.run(f'{APP_NAME.upper()}_SECRET=tardis FLASK_APP={AUTOAPP} flask {command}', echo=True)


@task(pre=[clean, build], post=[clean])
def test(ctx):
    """Run lint commands and tests."""
    ctx.run('cp myflaskapp/Pipfile .', echo=True)
    ctx.run('cp myflaskapp/Pipfile.lock .', echo=True)
    ctx.run('pipenv install --dev', echo=True)
    ctx.run('rm Pipfile', echo=True)
    ctx.run('rm Pipfile.lock', echo=True)
    _run_npm_command(ctx, 'run lint')
    os.chdir(COOKIE)
    _run_flask_command(ctx, 'lint')
    _run_flask_command(ctx, 'test')

@task
def readme(ctx, browse=False):
    ctx.run("rst2html.py README.rst > README.html")
    if browse:
        webbrowser.open_new_tab('README.html')

