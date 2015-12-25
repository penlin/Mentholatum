#-*- coding:utf-8 -*-
import sys
import os
import json
import xlwt
import StringIO
from calendar import monthrange

def exportSchedule(result, year, month, fmt='csv'):
  weekdays, day = monthrange(year,month)
  if fmt == 'csv':
    strbuf = "名字"
    for d in xrange(1,day+1):
      strbuf += (","+str(d))
    for a,b in result["人班表"].iteritems():
      strbuf += ("\n"+a.encode("utf-8")+","+",".join(b))
    return strbuf
  elif fmt == 'excel':
    f = StringIO.StringIO() # create a file-like object
    wbk = xlwt.Workbook()
    wbk.add_sheet('foo')
    sheet = wbk.get_sheet(0)
    sheet.write(0, 0, 'bar')
    wbk.save(f) 
    f.seek(0)
    return f.getvalue()
  else :
    print "Request export format ({0}) is not supported.".format(fmt)
    return None;
  
