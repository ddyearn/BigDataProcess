#!/usr/bin/python3
import sys
import datetime

with open(sys.argv[1], "rt") as f:
	data = f.read()

elements = []
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
dict = {}

rows = data.split("\n")
for row in rows:
	fields = row.split(",")
	dt = datetime.datetime.strptime(fields[1], '%m/%d/%Y')
	day = dt.weekday()
	element = (fields[0], days[day], int(fields[2]), int(fields[3]))
	elements.append(element)

for e in elements:
	k = '%s,%s' % (e[0], e[1])
	if k in dict:
		dict[k][0] += e[2]
		dict[k][1] += e[3]
	else:
		dict[k] = [e[2], e[3]]

keylist = dict.keys()
for key in keylist:
	print('%s %d,%d' % (key, dict[key][0], dict[key][1]))
