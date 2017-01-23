#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   16/3/24 下午12:43
#   Desc    :   PyHub
import uuid
import logging
import functools
from datetime import datetime
from logging.handlers import RotatingFileHandler

from peewee import fn, IntegrityError
from playhouse.flask_utils import FlaskDB
from flask import Flask, render_template, redirect, request, flash, abort
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField
from wtforms.validators import InputRequired, URL
from wtforms.widgets import TextArea
from config import DEBUG, SECRET_KEY, STATIC_PATH, LOG_FILENAME, PASSWORD

from model import Blog, database


app = Flask(__name__)
app.static_folder = STATIC_PATH
app.debug = DEBUG
app.secret_key = SECRET_KEY
csrf = CSRFProtect()
csrf.init_app(app)
FlaskDB(app, database)

handler = RotatingFileHandler(LOG_FILENAME, maxBytes=10000000, backupCount=5)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


class BlogForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    url = StringField('url', validators=[URL()])
    description = StringField('description', widget=TextArea())


def login(f):
    @functools.wraps(f)
    def warp_fun(*args, **kwargs):
        if PASSWORD != request.values.get('password'):
            abort(404)
        else:
            return f(*args, **kwargs)
    return warp_fun


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def home():
    all_blog = Blog.select().where(Blog.status == 1).order_by(fn.Random())
    app.logger.info('get blog total|%s' % len(all_blog))
    return render_template('blog.html', blogs=all_blog)


@app.route('/manage/')
@login
def manage():
    all_blog = Blog.select().order_by(Blog.create_time.desc())
    form = BlogForm()
    app.logger.info('%s|request manage page' % request.remote_addr)
    return render_template('manage.html', blogs=all_blog, form=form)


@app.route('/manage/create/', methods=['POST'])
@login
def create():
    form = BlogForm()
    if form.validate_on_submit():
        try:
            blog = Blog.create(
                blog_id=uuid.uuid4(), name=form.name.data, url=form.url.data,
                description=form.description.data)
            flash(u'创建 {name} 成功'.format(name=blog.name))
        except IntegrityError:
            flash(u'创建 {name} 失败，该条目已存在'.format(name=form.name.data), 'error')
    else:
        flash(u'创建失败，参数错误', 'error')
    return redirect('/manage')


@app.route('/manage/update/<blog_id>', methods=['GET', 'POST'])
@login
def update(blog_id):
    blog = Blog.get(Blog.blog_id == blog_id)
    if not blog:
        abort(400)
    form = BlogForm(name=blog.name, url=blog.url, description=blog.description)

    if request.method == 'GET':
        return render_template('update.html', blog=blog, form=form)
    else:
        if form.validate_on_submit():
            try:
                blog.name = form.name.data
                blog.url = form.url.data
                blog.description = form.description.data
                blog.update_time = datetime.now()
                blog.save()
                flash(u'更新 {name} 成功'.format(name=form.name.data))
                return redirect('/manage')
            except IntegrityError:
                flash(u'更新 {name} 失败，该条目已存在'.format(name=form.name.data), 'error')
                return render_template('update.html', blog=blog, form=form)
        else:
            flash(u'更新失败，参数错误', 'error')
            return render_template('update.html', blog=blog, form=form)


@app.route('/manage/status/<blog_id>', methods=['GET'])
@login
def status(blog_id):
    blog = Blog.get(Blog.blog_id == blog_id)
    if not blog:
        abort(400)
    if blog.status:
        blog.status = 0
        flash(u'{name}下线成功'.format(name=blog.name))
    else:
        blog.status = 1
        flash(u'{name}上线成功'.format(name=blog.name))
    blog.update_time = datetime.now()
    blog.save()
    return redirect('/manage')

if __name__ == '__main__':
    app.run(port=5000)

