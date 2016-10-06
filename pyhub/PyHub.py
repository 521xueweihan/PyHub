#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/3/24 下午12:43
#   Desc    :   python-blog-page
from os import path
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
app.static_folder = path.join(path.dirname(__file__), 'static')
app.debug = False


@app.route('/')
def home():
    return redirect(url_for('blog'))



@app.route('/blog')
def blog():
    return render_template('blog.html')

#
# @app.route('/manage')
# def manage():
#     return render_template('manage.html')

if __name__ == '__main__':
    app.run(port=5000)

