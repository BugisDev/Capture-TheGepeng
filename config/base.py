""" Base Configuration """

import os

APP_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

SECRET_KEY = 'g3p3ng 1s my n4m3'
ASSETS_DEBUG = False
CACHE_TYPE = 'simple'

# SECURITY CONFIG
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'changetowhateveryouwant'
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'changetowhateveryouwant'

# DATABASE CONFIG
SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/gepeng'
