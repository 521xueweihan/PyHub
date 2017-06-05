#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   
#   Author  :   XueWeiHan
#   Date    :   17/6/2 下午4:37
#   Desc    :   base

from peewee import Model, SqliteDatabase

from config import DATABASE_PATH

database = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    class Meta:
        database = database
        
