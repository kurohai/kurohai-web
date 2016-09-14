
import os
from dicto import dicto

class config(dicto):
    appname = 'Evan Burt'
    appnamed = 'kuroweb'
    pwd = os.path.abspath(os.curdir)
    SECRET_KEY = 'enydM2ANhdcoKwdVa0jWvEsbPFuQpMjf'
    SESSION_PROTECTION = 'strong'
    dbpath = '{dir}/{app}.db'.format(dir=pwd, app=appnamed)
    dburi = 'sqlite:///{db}'.format(db=dbpath)

