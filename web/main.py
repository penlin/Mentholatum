#-*- coding:utf-8 -*-

import os
import ws_api
from bottle import route, run, template



if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='0.0.0.0', port=port, debug=False)

