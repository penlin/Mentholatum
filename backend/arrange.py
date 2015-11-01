#-*- coding: utf-8 -*-

import os
import json
import sys
import codecs

from calendar import monthrange

class_key = ['白班', '小夜', '大夜']
num_constraint = {'白班': 3, '小夜': 3, '大夜': 2}

def arrange(nurse_path, year, month):
  days = monthrange(year, month)[1]
  print days
  results = dict()
  for x in xrange(1, days+1):
    results[x] = {'白班': list(), '小夜': list(), '大夜': list()}

  names = list()
  levels = dict()
  offday_dict = dict()

  with codecs.open(nurse_path, 'r', encoding='utf-8') as f:
    for line in f:
      if line.strip() == '':  continue
      x = line.strip().split(',')
      print x
      names.append(x[0])
      levels[x[0]] = x[1]
      offday_dict[x[0]] = x[2:]

  # TODO(Bruce Kuo): Arrange
  for name in names:
    continue_days = 0;
    offday_list = []
    for x in offday_dict[name]:
      offday_list.append(int(x))
    for day in xrange(1, days+1):
      if day in offday_list or continue_days >= 5:
        continue_days = 0
        continue
      for key in class_key:
        if len(results[day][key]) < num_constraint[key]:
          results[day][key].append(name)
          continue_days += 1

  #print results
  print json.dumps(results)
  return results


if __name__ == '__main__':
  if len(sys.argv) < 4:
    print "Usage: %s [nurse_path] [year] [month]" % (sys.argv[0])
  nurse_path = sys.argv[1]
  year = int(sys.argv[2])
  month = int(sys.argv[3])
  arrange(nurse_path, year, month)

