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
    wbk.add_sheet(("{0}-{1} ".format(year,month)+"人班表").decode("utf-8"))
    sheet = wbk.get_sheet(0)
    sheet.write(0, 0, "名字".decode("utf-8"))
    for d in xrange(1, day+1):
      sheet.write(0, d, str(d))
    curRow = 1
    for a,b in result["人班表"].iteritems():
      sheet.write(curRow,0,a)
      for d in xrange(1, day+1):
        sheet.write(curRow, d, b[d-1])
      curRow = curRow +1;
    wbk.save(f) 
    f.seek(0)
    return f.getvalue()
  else :
    print "Request export format ({0}) is not supported.".format(fmt)
    return None;
  
