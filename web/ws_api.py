#-*- coding:utf-8 -*-

import os
from bottle import route, template, request

@route('/ws/calendar/<month>')
def get_calendar(month):
  user = request.GET.get('user', None)

  return str(user)

