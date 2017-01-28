#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   Date    :   17/1/22 下午11:44
#   Desc    :   检测记录的blog访问速度，0为超时
#   http://stackoverflow.com/questions/11159687/measure-website-load-time-with-python-requests
import logging
import os

import requests
from model import Blog, database

logging.basicConfig(
    level=logging.WARNING,
    filename=os.path.join(os.path.dirname(__file__), 'network_script.log'),
    filemode='a',
    format='%(name)s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
)
logger = logging.getLogger('Script')  # 设置log名称


def get_load_time():
    """Measure website load time"""
    with database.execution_context() as ctx:
        all_blog = Blog.select()
        for blog in all_blog:
            try:
                speed_seconds = requests.get(blog.url, timeout=5).elapsed.total_seconds()
                blog.network = speed_seconds
                blog.save()
            except Exception:
                logger.error('Timeout: name|%s|url|%s' % (blog.name, blog.url))


get_load_time()