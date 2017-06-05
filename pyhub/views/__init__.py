#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/6/2 下午4:34
#   Desc    :   views
import functools

from flask import session, abort, render_template

from config import PASSWORD
from server import app


def login(f):
    @functools.wraps(f)
    def warp_fun(*args, **kwargs):
        if PASSWORD != session.get('password'):
            abort(404)
        else:
            return f(*args, **kwargs)
    return warp_fun


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
