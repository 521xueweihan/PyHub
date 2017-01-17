#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   Date    :   17/1/7 下午11:35
#   Desc    :   config
from os import path

DEBUG = True
DATABASE_PATH = path.join(path.dirname(__file__), 'blog.db')
SECRET_KEY = '2-123-102opi1po2i'
STATIC_PATH = path.join(path.dirname(__file__), 'static')