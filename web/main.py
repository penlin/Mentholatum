#-*- coding:utf-8 -*-
import sys
sys.path.append('../../');

import os
import ws_api
import json
from bottle import route, run, template, get, static_file, post, request, redirect, abort
from Mentholatum.backend.arrange import *
from calendar import IllegalMonthError

@route('/js/<filename:re:.*\.js>')
def javascript(filename):
	return static_file(filename, root='js')

@route('/img/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='img')

@route('/css/<filename:re:.*\.css>')
def stylesheet(filename):
	return static_file(filename, root='css')

@get('/')
def test():
  schedule = [] # place holder
  schedule.append({'title':'Test Event 1 Blue','start':'2015-10-25T21:00:00','end':'2015-10-26T02:00:00','color':'#33F'})
  schedule.append({'title':'Test Event 2 Red','start':'2015-10-10T02:00:00','end':'2015-10-10T07:00:00','color':'#F33'})
  return template('tpl/mentholatum',schedule_json_arr=json.dumps(schedule))

@post('/do_upload')
def do_upload():
  upload = request.files.get('upload')
  name, ext = os.path.splitext(upload.filename)
  if ext not in ('.csv','.txt'):
    # redirect to error page or the original page
    return 'File extension not allowed.'
  date = request.forms.get('upload_month');
  print '[INFO] upload configuration file for month:',date;
  save_path = './upload-' + date;
  upload.save(save_path)

  redirect("/"+date);

@get('/<year>-<month>')
def tbl_layout(year, month):
  """
  result = dict()
  result['穴宇'] = list()
  result['魯斯'] = list()
  for idx in xrange(1, 9):
    result['穴宇'].append('11-7')
    result['魯斯'].append('7-3')
  for idx in xrange(9, 17):
    result['穴宇'].append('3-11')
    result['魯斯'].append('OFF')
  for idx in xrange(17, 25):
    result['穴宇'].append('OFF')
    result['魯斯'].append('11-7')
  for idx in xrange(25,32):
    result['穴宇'].append('7-3')
    result['魯斯'].append('3-11')
  """

  try:
    result = arrange('./upload-'+year+'-'+month, int(year), int(month))
    return template('tpl/mentholatum-tbl', result_json = json.dumps(result["人班表"]), m_year = year, m_month = month)
  except IllegalMonthError:
    abort(404,"Request month is not found.")
  except IOError as e:
    if e.errno is not 2:
      abort(404, "IOError {0}:{1}".format(e.errno, e.strerror))
    return template('tpl/mentholatum-tbl', result_json = json.dumps(dict()), m_year = year, m_month = month)
  except :
    abort(500,"Sorry for internel error.\n error:" + sys.exc_info()[0].__name__)


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8080))
  run(host='0.0.0.0', port=port, debug=False)

