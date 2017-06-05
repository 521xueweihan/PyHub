#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   16/3/24 下午12:43
#   Desc    :   run
from playhouse.flask_utils import FlaskDB
from flask.sessions import SecureCookieSessionInterface
from flask_wtf import CSRFProtect
from config import DEBUG, SECRET_KEY, STATIC_PATH, SESSION_COOKIE_SECURE

from models.base import database
from pyhub import app


app.static_folder = STATIC_PATH
app.debug = DEBUG
app.secret_key = SECRET_KEY
app.session_cookie_secure = SESSION_COOKIE_SECURE
app.session_interface = SecureCookieSessionInterface()

csrf = CSRFProtect()
csrf.init_app(app)
FlaskDB(app, database)

if __name__ == '__main__':
    app.run(port=5000)

