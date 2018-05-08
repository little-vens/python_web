#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import time, uuid

from www.orm import Model, StringFeild, BooleanFeild, FloatFeild, TextFeild

def next_id():
	return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringFeild(primary_key=True, default=next_id, ddl='varchar(50)')
	email =StringFeild(ddl='varchar(50)')
	passwd = StringFeild(ddl='varchar(50)')
	admin = BooleanFeild()
	name = StringFeild(ddl='varchar(50)')
	image = StringFeild(ddl='varchar(500)')
	created_at = FloatFeild(default=time.time)

class Blog(Model):
	"""docstring for Blog"""
	__table__ = 'blogs'

	id = StringFeild(primary_key=True, default=next_id, ddl='varchar(50)')
	user_id =StringFeild(ddl='varchar(50)')
	user_name = StringFeild(ddl='varchar(50)')
	name = StringFeild(ddl='varchar(50)')
	user_image = StringFeild(ddl='varchar(500)')
	summary = StringFeild(ddl='varchar(200)')
	content = TextFeild()
	created_at = FloatFeild(default=time.time)
	
class Comment(Model):

	__table__ = 'comments'

	id = StringFeild(primary_key=True, default=next_id, ddl='varchar(50)')
	blog_id =StringFeild(ddl='varchar(50)')
	user_id = StringFeild(ddl='varchar(50)')
	user_name = StringFeild(ddl='varchar(50)')
	user_image = StringFeild(ddl='varchar(500)')
	content = TextFeild()
	created_at = FloatFeild(default=time.time)