#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   16/3/24 下午12:43
#   Desc    :   python-blog-page
from os import path

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, URL

from model import Blog


app = Flask(__name__)
app.static_folder = path.join(path.dirname(__file__), 'static')
app.debug = True
app.secret_key = 'asdfsfsadf'


class BlogForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    url = StringField('url', validators=[URL()])
    description = StringField('description')


@app.route('/')
def home():
    return render_template('blog.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/manage')
def manage():
    blogs = Blog.select().where(Blog.status == 1)
    form = BlogForm()
    return render_template('manage.html', blogs=blogs, form=form)


@app.route('/manage/create', methods=['POST'])
def create():
    blog = Blog()
    form = BlogForm()
    if form.validate_on_submit():
        blog.name = form.name.data
        blog.url = form.url.data
        blog.description = form.description.data
        blog.save()
        return redirect('/manage')


@app.route('/manage/update', methods=['GET', 'POST'])
def update():
    pass

@app.route('/manage/delete', methods=['POST'])
def delete():
    pass

#
# @app.route('/manage')
# def manage():
#     return render_template('manage.html')

if __name__ == '__main__':
    app.run(port=5000)

