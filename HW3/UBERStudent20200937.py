import sys, calendar

uberList = []
dayOfWeek = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}

with open(sys.argv[1], "rt") as f:
	while True:
		row = f.readline()
		if not row: break
		
		fields = row.split(",")
	
		base = fields[0]
		
		dt = fields[1].split("/")
		day = days[calendar.weekday(int(dt[0]), int(dt[1]), int(dt[2]))]
	
		vehicle = int(fields[2])
		trip = int(fields[3])
	
		flag = 0
		for uber in uberList:
			if uber[0] == base and uber[1] == day:
				uber[2] += vehicle
				uber[3] += trip
				flag = 1
				break
			
		if flag == 0:
			uberList.append([base, day, vehicle, trip])
			
		fp = open(sys.argv[2], "wt")
		for item in uberList:
			fp.write("%s,%s %d,%d\n" %(item[0], item[1], item[2], item[3]))
		fp.close()


