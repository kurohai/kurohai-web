from flask import Blueprint
from flask import render_template, request, url_for, send_file
from dicto import dicto
from sqlalchemy import and_
from pprint import pprint
import codecs
import os
from flaskapp import *


blueprint = Blueprint(flasktemplate.appnamed, __name__)

@blueprint.route('/poetry/')
def about():
    return render_template('public/about.html')

@blueprint.route('/')
def home():
    return render_template('public/index.html')

@blueprint.route('/voice.xml', methods=['GET', 'POST'])
def voice():
    return send_file('templates/voice.xml')
