#-*- coding: utf-8 -*-

import os
import json
import sys
import codecs

from calendar import monthrange

def arrange(nurse_path, year, month):
  days = monthrange(year, month)
  results = dict()
  for x in xrange(1:days+1):
    results[x] = {'白班': list(), '小夜': list(), '大夜': list()}

  names = list()
  levels = dict()
  offday_dict = dict()

  with codecs.open(nurse_path, 'r', encoding='utf-8') as f:
    for line in f:
      x = line.strip().split(',')
      names.append(x[0])
      levels[x[0]] = x[1]
      offday_dict[x[0]] = x[2:]

  # TODO(Bruce Kuo): Arrange

  return results


if __name__ == '__main__':
  if len(sys.argv) < 4:
    print "Usage: %s [nurse_path] [year] [month]" % (sys.argv[0])
  nurse_path = sys.argv[1]
  year = sys.argv[2]
  month = sys.argv[3]
  arrange(nurse_path, year, month)

