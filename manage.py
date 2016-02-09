import os
import cherrypy
from cherrypy import wsgiserver
from cherrypy.process.plugins import Daemonizer,PIDFile
from flask.ext.script import Manager
from flaskapp import flasktemplate, Base, engine
from colord import engine, Color, ColorSet, session
from colord import Base as colord_base
from colord import flasktemplate as colord_flasktemplate


manager = Manager(flasktemplate)


@manager.command
def db():
    Base.metadata.create_all(bind=engine)
    colord_base.metadata.drop_all(bind=engine)
    colord_base.metadata.create_all(bind=engine)
    data()


@manager.command
def quick():
    d = wsgiserver.WSGIPathInfoDispatcher({'/kurohai': flasktemplate, '/colord': colord_flasktemplate})
    server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 80), d, server_name=flasktemplate.appname, )
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


@manager.command
def go():
    flasktemplate.run(debug=True, host='0.0.0.0', port=80)

@manager.command
def colord():
    colord_flasktemplate.run(debug=True, host='0.0.0.0', port=80)



def data():
    day = ColorSet()

    yellow = Color()
    yellow.name = 'yellow'
    yellow.colorset = day

    white = Color()
    white.name = 'white'
    white.colorset = day

    pink = Color()
    pink.name = 'pink'
    pink.colorset = day

    purple = Color()
    purple.name = 'purple'
    purple.colorset = day

    olive = Color()
    olive.name = 'olive'
    olive.colorset = day

    azure = Color()
    azure.name = 'azure'
    azure.colorset = day

    camo = Color()
    camo.name = 'camo'
    camo.colorset = day

    session.add(day)
    session.add(yellow)
    session.add(white)
    session.add(pink)
    session.add(purple)
    session.add(olive)
    session.add(azure)
    session.add(camo)
    session.commit()


if __name__ == '__main__':
    manager.run()
