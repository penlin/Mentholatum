#-*- coding:utf-8 -*-
import sys
import os
import time
import json

def parseExportParamFromQuery(queryDict):
  if 'year' in queryDict:
    year = queryDict['year']
  else :
    year = time.strftime("%Y")
  if 'month' in queryDict:
    month = queryDict['month']
  else :
    month = time.strftime("%m")
  if 'fmt' in queryDict:
    fmt = queryDict['fmt'].lower()
  else :
    fmt = 'csv'
  return year,month,fmt
