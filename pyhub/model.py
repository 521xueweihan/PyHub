#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   Date    :   16/9/30 下午11:05
#   Desc    :   数据层
import os
import random
import uuid
from datetime import datetime

from peewee import Model, SqliteDatabase, CharField, TextField, \
    DateTimeField, IntegerField

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'test.db')
database = SqliteDatabase(DATABASE_PATH)


def next_id():
    """
    使用random函数随机生成一个长度为10的纯数字字符串
    """
    chars = '0123456789'
    uid = random.sample(chars, 8)
    return int(''.join(uid))


class BaseModel(Model):
    class Meta:
        database = database


class Blog(BaseModel):
    id = CharField(default=next_id(), primary_key=True)
    name = CharField()
    url = CharField()
    description = TextField()
    create_time = DateTimeField(default=datetime.now())
    update_time = DateTimeField(default=datetime.now())
    status = IntegerField(default=0)

database.create_tables([Blog], safe=True)