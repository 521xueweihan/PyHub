#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   Date    :   16/9/30 下午11:05
#   Desc    :   数据层
import os
import sqlite3

from peewee import Model, SqliteDatabase, CharField, TextField, \
    DateTimeField, IntegerField

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'test.db')
database = SqliteDatabase(DATABASE_PATH)


class BaseModel(Model):
    class Meta:
        database = database


class Blog(BaseModel):
    name = CharField()
    url = CharField()
    description = CharField()
    create_time = DateTimeField()
    update_time = DateTimeField()
    status = IntegerField()

# print "Opened database successfully"
# conn.execute('''CREATE TABLE blog
#        (id INTEGER PRIMARY KEY,
#        name        CHAR(100)    NOT NULL,
#        url         CHAR(500)     NOT NULL,
#        type        CHAR(10));''')
# print "Table created successfully"

# conn.execute("INSERT INTO blog (name,url,type) \
#       VALUES ('Paul', 'http://www.baidu.com', 'California')")
#
# conn.commit()
# cursor = conn.execute("SELECT id, name, url, type  from blog")
# for row in cursor:
#    print "ID = ", row[0]
#    print "NAME = ", row[1]
#    print "URL = ", row[2]
#    print "TYPE = ", row[3], "\n"
# conn.close()