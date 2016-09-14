from sqlalchemy.orm import scoped_session, sessionmaker
from flaskapp import app, Base, User, session, engine, log, Log
import time
from flaskapp.secret import Admin


def initdb():
    Base.metadata.create_all(bind=engine)
    log.warn('tables created')
    print 'tables created'
    mkusr()
    log.info('user created')
    print 'user created'


def deldb():
    try:
        log.warn('tables deleted')
    except:
        pass
    print 'tables deleted'
    try:
        Base.metadata.drop_all(bind=engine)
    except:
        pass


def mkusr():
    print 'adding user'

    u = User()
    a = Admin()

    u.username = a.username
    u.id = a.id
    u.email = a.email
    u.password = a.password
    u.admin = a.admin

    session.add(u)
    session.commit()


if __name__ == '__main__':
    deldb()
    initdb()
