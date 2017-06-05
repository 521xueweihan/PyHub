#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/6/2 下午4:35
#   Desc    :   首页
from flask import request, render_template, session
from peewee import fn


from pyhub import app, logger
from models.blog import Blog
from config import PASSWORD


@app.route('/')
def home():
    all_blog = Blog.select().where(Blog.status == 1).order_by(fn.Random())
    logger.info('get blog total|%s' % len(all_blog))
    if request.values.get('password') == PASSWORD:
        session['password'] = PASSWORD
    return render_template('blog.html', blogs=all_blog)