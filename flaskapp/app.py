#!/bin/env python

from flask import Flask
# from flask.ext.pagedown import PageDown
# from flaskext.markdown import Markdown
from settings import config
from handlers import SQLAlchemyHandler
import logging

appname = config.appname
appnamed = config.appnamed
pwd = config.pwd


flasktemplate = Flask(__name__)
flasktemplate.appname = config.appname
flasktemplate.appnamed = config.appnamed
flasktemplate.secret_key = config.SECRET_KEY
flasktemplate.session_protection = config.SESSION_PROTECTION


handler = SQLAlchemyHandler()
handler.setLevel(logging.DEBUG)
flasktemplate.logger.addHandler(handler)
log = flasktemplate.logger


# pagedown = PageDown(flasktemplate)
# Markdown(flasktemplate)


@flasktemplate.template_global()
def appname():
    return flasktemplate.appname


@flasktemplate.template_global()
def appnamed():
    return flasktemplate.appnamed


@flasktemplate.errorhandler(404)
def error_not_found(error):
    """Render a custom template when responding with 404 Not Found."""
    return 'No page here, dood. 404!', 404
