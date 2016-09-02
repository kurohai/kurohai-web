from flask import Blueprint, redirect
from flask import render_template, request, url_for, send_file, send_from_directory
from flask.ext.login import LoginManager, current_user
from flask.ext.login import login_user, login_required, logout_user

from dicto import dicto
from sqlalchemy import and_
from pprint import pprint
import codecs
import os
from flaskapp import *


blueprint = Blueprint(flasktemplate.appnamed, __name__)


@blueprint.route('/poetry/')
def poetry():
    return render_template('public/poetry.html')


@blueprint.route('/')
def home():
    log.info(current_user.username)
    return render_template('public/index.html')


@blueprint.route('/voice.xml', methods=['GET', 'POST'])
def voice():
    return send_file('templates/voice.xml')


@blueprint.route('/resume/python-dev/')
@login_required
def python_dev():
    return render_template('public/resume/python-dev.html')


@blueprint.route('/wiki/<path:path>')
@login_required
def wiki(path):
    log.info(path)
    log.info(current_user.username)
    fullpath = os.path.abspath(os.curdir) + '/flaskapp/templates/wiki/'
    print 'full path: {0}{1}'.format(fullpath, path)
    if os.path.isdir(os.path.join(fullpath, path)):
        path = path + 'index.html'
        log.info('full path: {0}{1}'.format(fullpath, path))
        print 'full path: {0}{1}'.format(fullpath, path)

    return send_from_directory(fullpath, path)


@blueprint.route('/wiki/')
@login_required
def wiki_home():
    log.info('no file ext redirect')
    return wiki('index.html')


@blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('kuroweb.home'))
    form = LoginForm(request.form)
    error = None

    log.info(current_user.username)

    # form validation not working
    # if request.method == 'POST' and form.validate():
    if request.method == 'POST':
        email = form.username.data.lower().strip()
        password = form.password.data.lower().strip()
        user, authenticated = \
            User.authenticate(session.query, email, password)
        if authenticated:
            login_user(user)
            return redirect(url_for('kuroweb.home'))
        else:
            error = 'Incorrect username or password. Try again.'
    else:
        log.info('request method: ' + request.method)
        log.info('form.validate(): ' + str(form.validate()))
    return render_template('user/login.html', form=form, error=error)

@blueprint.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('kuroweb.home'))
