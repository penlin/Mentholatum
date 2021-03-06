#-*- coding:utf-8 -*-
import sys
sys.path.append('../../');

import os
import time
import ws_api
import utils
import json
from download import exportSchedule
from bottle import route, run, template, get, static_file, post, request, response, redirect, abort
from Mentholatum.backend.arrange import *
from calendar import IllegalMonthError, monthrange

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
def default():
  # temporarily use table style as default
  redirect(time.strftime("/%Y-%m"))
  
  # Following code is the test data for calendar style
  """
  schedule = [] # place holder
  schedule.append({'title':'Test Event 1 Blue','start':'2015-10-25T21:00:00','end':'2015-10-26T02:00:00','color':'#33F'})
  schedule.append({'title':'Test Event 2 Red','start':'2015-10-10T02:00:00','end':'2015-10-10T07:00:00','color':'#F33'})
  return template('tpl/mentholatum',schedule_json_arr=json.dumps(schedule))
  """

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
  upload.save(save_path, overwrite=True);
  redirect("/"+date);

@get('/export')
def export():
  year,month,fmt = utils.parseExportParamFromQuery(request.query.decode())
  try:
    iyear = int(year)
    imonth = int(month)
    result = arrange('./upload-'+year+'-'+month, iyear, imonth)
  except IllegalMonthError:
    abort(404,"Request file is not found.")
  except IOError as e:
    if e.errno is not 2:
      abort(404,"IOError {0}:{1}".format(e.errno, e.strerror))
    else:
      abort(404,"Request file is not found.")
  except:
    abort(500,"Internal error.")
  else:
    buf = exportSchedule(result, iyear, imonth, fmt)
    if buf == None:
      print 'exportSchedule return result None.'
      abort(500, "Internal error.")

    print '[INFO] export schedule of ', year, '-',month, ' in ', fmt , ' format.'
    #print buf
    if fmt == 'csv':
      response.headers['Content-Type'] = 'text/csv; charset=UTF-8'
      response.headers['Content-Disposition'] = 'attachment; filename="schedule' + year + '' + month + '.csv"'
    elif fmt == 'excel':
      response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=UTF-8'
      response.headers['Content-Disposition'] = 'attachment; filename="schedule' + year + '' + month + '.xlsx"' 
    return buf

@get('/<year>-<month>')
def tbl_layout(year, month):
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

