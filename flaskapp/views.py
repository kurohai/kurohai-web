from flask import Blueprint, redirect
from flask import render_template, request, url_for, send_file, send_from_directory
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
    return render_template('public/index.html')


@blueprint.route('/voice.xml', methods=['GET', 'POST'])
def voice():
    return send_file('templates/voice.xml')


@blueprint.route('/resume/python-dev/')
def python_dev():
    return render_template('public/resume/python-dev.html')


@blueprint.route('/wiki/<path:path>')
def wiki(path):
    print path
    fullpath = os.path.abspath(os.curdir) + '/flaskapp/templates/wiki/'
    if os.path.isdir(os.path.join(fullpath, path)):
        path = path + 'index.html'
        print 'last one:', fullpath

    return send_from_directory(fullpath, path)


@blueprint.route('/wiki/')
def wiki_home():
    return wiki('index.html')
