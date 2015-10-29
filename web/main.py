#-*- coding:utf-8 -*-

import os
import ws_api
import json
from bottle import route, run, template, get

@get('/')
def test():
  schedule = [] # place holder
  schedule.append({'title':'Test Event 1 Blue','start':'2015-10-25T21:00:00','end':'2015-10-26T02:00:00','color':'#33F'})
  schedule.append({'title':'Test Event 2 Red','start':'2015-10-10T02:00:00','end':'2015-10-10T07:00:00','color':'#F33'})
  return template('tpl/mentholatum',schedule_json_arr=json.dumps(schedule))

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='0.0.0.0', port=port, debug=False)

