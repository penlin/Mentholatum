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
N = 'N'
SR_list = ['N2', 'N4']
output_format = {'白班': "7-3'", '小夜': "3-11'", '大夜': "11-7'"}
week_day = {0: '日', 1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六'}

def arrange(nurse_path, year, month):
  #print monthrange(year, month)
  weekday, days = monthrange(year, month)
  #print weekday, days
  results = dict()
  for x in xrange(1, days+1):
    results[x] = {'白班': list(), '小夜': list(), '大夜': list()}

  names = list()
  levels = dict()
  reserved_class = dict()
  offday_dict = dict()
  personal_class_info = dict()
  offday_info = dict()
  bau_class = dict()
  continue_days = dict()

  #initialize
  with codecs.open(nurse_path, 'r', encoding='utf-8') as f:
    for line in f:
      if line.strip() == '':  continue
      x = line.strip().split(',')
      #print ",".join(x)
      names.append(x[0])
      levels[x[0]] = x[1]
      reserved_class[x[0]] = x[2]
      bau_class[x[0]] = 0
      offday_dict[x[0]] = x[5:]
      offday_info[x[0]] = {"off": 0, "weekend": 0}
      continue_days[x[0]] = int(x[3])
      personal_class_info[x[0]] = dict()

  op = list(names)
  
  weekend_off = dict()
  for name in names:
    #continue_days[name] = 0
    weekend_off[name] = 0
    

  for day in xrange(1, days+1):
    random.shuffle(names)
    for name in names:
      offday_list = []
      if name.encode('utf-8') == '陳嬿菱' and (day > 15):
          continue
      for x in offday_dict[name]:
        offday_list.append(int(x))
      # 最多五天休一天
      #print offday_list
      if day in offday_list or continue_days[name] >= 5:
        #continue_days[name] = 0
        continue

      # 天數太多, 休假
      if len(personal_class_info.keys()) >= days - 8:
        #continue_days[name] = 0
        continue

      #包班優先
      if reserved_class[name].encode('utf-8') != 'N' and bau_class[name] < 20 and \
        len(results[day][reserved_class[name].encode('utf-8')]) < num_constraint[reserved_class[name].encode('utf-8')]:
        
        results[day][reserved_class[name].encode('utf-8')].append(name)
        personal_class_info[name][day] = reserved_class[name].encode('utf-8')
        continue_days[name] += 1
        bau_class[name] += 1
        continue

    for name in names:
      if personal_class_info[name].has_key(day):
        continue
      offday_list = []
      if name.encode('utf-8') == '陳嬿菱' and (day > 15):
          continue
      for x in offday_dict[name]:
        offday_list.append(int(x))
      # 最多五天休一天
      #print offday_list
      if day in offday_list or continue_days[name] >= 5:
        continue_days[name] = 0
        continue

      # 天數太多, 休假
      if len(personal_class_info.keys()) >= days - 8:
        continue_days[name] = 0
        continue

      hasClass = False
      for key in class_key:
        if name.encode('utf-8') == '陳嬿菱' and (key != '白班' or day > 15):
          continue
        if len(results[day][key]) < num_constraint[key]:
          # 一天不能排兩班以上
          if personal_class_info[name].has_key(day):
            continue
          
          # 大夜不接白班
          if key == BB and \
             personal_class_info[name].has_key(day-1) and \
             personal_class_info[name][day-1] == DN:
             continue;

          # 包大夜不上小夜
          if key == SN and reserved_class[name].encode('utf-8') == DN:
            continue

          # 包小夜不上大夜
          if key == DN and reserved_class[name].encode('utf-8') == SN:
            continue

          # 至少一個Sr
          if len(results[day][key]) == 0 and levels[name] not in SR_list:
            continue_days[name] = 0
            continue

          results[day][key].append(name)
          personal_class_info[name][day] = key
          for y in xrange(day-7, day):
            if not personal_class_info.has_key(y):
              break

          continue_days[name] += 1
          hasClass = True
          if key == reserved_class[name].encode('utf-8'):
            bau_class[name] += 1
      if not hasClass:
        continue_days[name] = 0

  
  # 回補
  for day in xrange(1, days + 1):
    for key in class_key:
      random.shuffle(names)
      for name in names:
        if name.encode('utf-8') == '陳嬿菱' and (key != '白班' or day > 15):
          continue
        if len(results[day][key]) < num_constraint[key] and \
          not personal_class_info[name].has_key(day):
          results[day][key].append(name)
          personal_class_info[name][day] = key
  

  results["人班表"] = dict()
  header = "人員"
  wkd = weekday
  for day in xrange(1, days + 1):
    header += "," + str(month) + "/" + str(day) + '(' + week_day[wkd%7] + ')'
    wkd += 1
  print header
  for x in op:
    if not personal_class_info.has_key(x):
      continue
    results["人班表"][x] = list()
    k = x
    v = personal_class_info[x]
    output = k
    wkd = weekday
    for day in xrange(1,days+1):
      if v.has_key(day):
        output += "," + output_format[v[day]]
        results["人班表"][k].append(output_format[v[day]])
      else:
        offday_info[x]['off'] += 1
        if wkd % 7 == 0 or wkd % 7 == 6:
          offday_info[x]['weekend'] += 1
        output += ",OFF"
        results["人班表"][k].append("OFF")
      wkd += 1
    #print len(output.split(','))
    output += ",休假:".decode('utf-8') + str(offday_info[x]['off'])
    output += ",週末休假:".decode('utf-8') + str(offday_info[x]['weekend'])
    print output.encode('utf-8')
  #print results

  with codecs.open("result.json", "w", encoding='utf-8') as f:
    for k,v in results.iteritems():
      print "day " + str(k)
      for a, b in v.iteritems():
        print a+",", ",".join(b).encode("utf-8")
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

