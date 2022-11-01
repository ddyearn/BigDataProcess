#!/usr/bin/python3
import sys
import calendar

with open(sys.argv[1], "rt") as f:
	data = f.read()

ubers = []
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

rows = data.split("\n")
for row in rows:
	fields = row.split(",")
	
	base = fields[0]
	
	dt = fields[1].split("/")
	day = days[calendar.weekday(int(dt[2]), int(dt[0]), int(dt[1]))]
	
	vehicle = int(fields[2])
	trip = int(fields[3])
	
	flag = 0
	
	for uber in ubers:
		if uber[0] == base and uber[1] == day:
			uber[2] += vehicle
			uber[3] += trip
			flag = 1
			break
			
	if flag == 0:
		ubers.append([base, day, vehicle, trip])

with open(sys.argv[2], "wt") as fp:
	for uber in ubers:
		fp.write('%s,%s %d,%d\n' % (uber[0], uber[1], uber[2], uber[3]))
		

