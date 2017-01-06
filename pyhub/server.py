#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   16/3/24 下午12:43
#   Desc    :   python-blog-page
from os import path

from model import Blog
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
app.static_folder = path.join(path.dirname(__file__), 'static')
app.debug = False


@app.route('/')
def home():
    return render_template('blog.html')


@app.route('/manage')
def manage():
    blogs = Blog.select().where(Blog.status == 1)
    return render_template('manage.html', blogs=blogs)

@app.route('/manage/create')
def create():
    pass

@app.route('/manage/update')
def update():
    pass

@app.route('/manage/delete')
def delete():
    pass


#
# @app.route('/manage')
# def manage():
#     return render_template('manage.html')

if __name__ == '__main__':
    app.run(port=5000)

