#-*- coding: utf-8 -*-

import os
import json
import sys
import codecs
import random

from calendar import monthrange

class_key = ['白班', '小夜', '大夜']
num_constraint = {'白班': 3, '小夜': 2, '大夜': 2}
DN = '大夜'
SN = '小夜'
BB = '白班'
SR_list = ['N2', 'N4', 'N']

def arrange(nurse_path, year, month):
  print monthrange(year, month)
  weekday, days = monthrange(year, month)
  print weekday, days
  results = dict()
  for x in xrange(1, days+1):
    results[x] = {'白班': list(), '小夜': list(), '大夜': list()}

  names = list()
  levels = dict()
  reserved_class = dict()
  offday_dict = dict()
  personal_class_info = dict()

  with codecs.open(nurse_path, 'r', encoding='utf-8') as f:
    for line in f:
      if line.strip() == '':  continue
      x = line.strip().split(',')
      #print ",".join(x)
      names.append(x[0])
      levels[x[0]] = x[1]
      reserved_class[x[0]] = x[2]
      offday_dict[x[0]] = x[3:]
      personal_class_info[x[0]] = dict()

  continue_days = dict()
  weekend_off = dict()
  for name in names:
    continue_days[name] = 0
    offday_list = []
    weekend_off[name] = 0
    for x in offday_dict[name]:
      offday_list.append(int(x))

  # TODO(Bruce Kuo): Arrange
  for day in xrange(1, days+1):
    random.shuffle(names)
    for name in names:
      # 最多五天休一天
      if continue_days[name] >= 5:
        continue_days[name] = 0
        continue

      # 天數太多, 休假
      if len(personal_class_info.keys()) >= days - 8:
        continue

      #包班優先
      if len(results[day][reserved_class[name].encode('utf-8')]) < num_constraint[reserved_class[name].encode('utf-8')]:
        results[day][reserved_class[name].encode('utf-8')].append(name)
        personal_class_info[name][day] = reserved_class[name].encode('utf-8')
        continue_days[name] += 1
        continue

      for key in class_key:
        if len(results[day][key]) < num_constraint[key]:
          # 一天不能排兩班以上
          if personal_class_info[name].has_key(day):
            continue_days[name] = 0
            continue
          
          # 大夜不接白班
          if key == BB and \
             personal_class_info[name].has_key(day-1) and \
             personal_class_info[name][day-1] == DN:
             continue_days[name] = 0
             continue;

          # 包大夜不上小夜
          if key == SN and reserved_class[name].encode('utf-8') == DN:
            continue_days[name] = 0
            continue

          # 包小夜不上大夜
          if key == DN and reserved_class[name].encode('utf-8') == SN:
            continue_days[name] = 0
            continue

          # 至少一個Sr

          results[day][key].append(name)
          personal_class_info[name][day] = key
          continue_days[name] += 1

  for k, v in personal_class_info.iteritems():
    print k, len(v)
  #print results
  with codecs.open("result.json", "w", encoding='utf-8') as f:
    for k,v in results.iteritems():
      print "day " + str(k)
      for a, b in v.iteritems():
        print a, ",".join(b)
    f.write(json.dumps(results))
  #print json.dumps(results)
  return results


if __name__ == '__main__':
  if len(sys.argv) < 4:
    print "Usage: %s [nurse_path] [year] [month]" % (sys.argv[0])
  nurse_path = sys.argv[1]
  year = int(sys.argv[2])
  month = int(sys.argv[3])
  arrange(nurse_path, year, month)

