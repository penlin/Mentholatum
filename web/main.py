#-*- coding:utf-8 -*-

import os
import ws_api
from bottle import route, run, template, get

@get('/')
def test():
  return template('tpl/mentholatum')

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='0.0.0.0', port=port, debug=False)

