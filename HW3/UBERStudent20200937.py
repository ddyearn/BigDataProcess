#!/usr/bin/python3
import sys
import datetime

with open(sys.argv[1], "rt") as f:
	data = f.read()

elements = []
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
dic = {}

rows = data.split("\n")
for row in rows:
	fields = row.split(",")
	dt = datetime.datetime.strptime(fields[1], '%m/%d/%Y')
	day = dt.weekday()
	element = (fields[0], days[day], int(fields[2]), int(fields[3]))
	elements.append(element)

for e in elements:
	k = '%s,%s' % (e[0], e[1])
	if k not in dic:
		dic[k] = [e[2], e[3]]
	else:
		dic[k][0] += e[2]
		dic[k][1] += e[3]

with open(sys.argv[2], "wt") as fp:
	keylist = dic.keys()
	for key in keylist:
		fp.write('%s %d,%d\n' % (key, dic[key][0], dic[key][1]))
		

