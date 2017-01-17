#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   Date    :   16/9/30 下午11:05
#   Desc    :   数据层
import uuid
from datetime import datetime

from peewee import Model, SqliteDatabase, CharField, TextField, \
    DateTimeField, IntegerField, UUIDField

from config import DATABASE_PATH
database = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class Blog(BaseModel):
    blog_id = UUIDField(unique=True)
    name = CharField(unique=True)
    url = CharField(unique=True)
    description = TextField()
    create_time = DateTimeField(default=datetime.now)
    update_time = DateTimeField(default=datetime.now)
    status = IntegerField(default=0)

database.create_tables([Blog], safe=True)