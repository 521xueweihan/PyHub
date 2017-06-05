#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/6/2 下午4:35
#   Desc    :   管理后台
import uuid
from datetime import datetime

from peewee import IntegrityError
from flask import render_template, redirect, request, flash, abort
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, URL
from wtforms.widgets import TextArea

from models.blog import Blog
from pyhub import app, logger
from views import login


class BlogForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])
    url = StringField('url', validators=[URL()])
    description = StringField('description', widget=TextArea())


@app.route('/manage/')
@login
def manage():
    all_blog = Blog.select().order_by(Blog.create_time.desc())
    form = BlogForm()
    logger.info('%s|request manage page' % request.remote_addr)
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