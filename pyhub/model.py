#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
#   Author  :   XueWeiHan
#   E-mail  :   595666367@qq.com
#   Date    :   16/9/30 下午11:05
#   Desc    :   数据层
import os
import sqlite3

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'test.db')

conn = sqlite3.connect(DATABASE_PATH)
# print "Opened database successfully"
# conn.execute('''CREATE TABLE blog
#        (id INTEGER PRIMARY KEY,
#        name        CHAR(100)    NOT NULL,
#        url         CHAR(500)     NOT NULL,
#        type        CHAR(10));''')
# print "Table created successfully"

conn.execute("INSERT INTO blog (name,url,type) \
      VALUES ('Paul', 'http://www.baidu.com', 'California')")

conn.commit()
cursor = conn.execute("SELECT id, name, url, type  from blog")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "URL = ", row[2]
   print "TYPE = ", row[3], "\n"
conn.close()