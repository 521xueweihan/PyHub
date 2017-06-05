#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   XueWeiHan
#   Date    :   16/9/30 下午11:05
#   Desc    :   数据层
from datetime import datetime

from peewee import Model, SqliteDatabase, CharField, TextField, \
    DateTimeField, IntegerField, UUIDField, FloatField

from models.base import BaseModel, database


class Blog(BaseModel):
    blog_id = UUIDField(unique=True)
    name = CharField(unique=True)
    url = CharField(unique=True)
    network = FloatField(default=0.0)
    description = TextField()
    create_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.now)
    status = IntegerField(default=0)

database.create_tables([Blog], safe=True)