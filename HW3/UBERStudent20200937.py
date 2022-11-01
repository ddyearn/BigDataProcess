import sys, calendar

uberList = []
dayOfWeek = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}

with open(sys.argv[1], "rt") as f:
	while True:
		line = f.readline()
		if not line: break
		
		info = line.split(",")
	
		region = info[0]
		
		date = info[1].split("/")
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
	
		vehicle = int(info[2])
		trip = int(info[3])
	
		flag = 0
		for uber in uberList:
			if uber[0] == region and uber[1] == day:
				uber[2] += vehicle
				uber[3] += trip
				flag = 1
				break
			
		if flag == 0:
			uberList.append([region, day, vehicle, trip])
			
		fp = open(sys.argv[2], "wt")
		for item in uberList:
			fp.write("%s,%s %d,%d\n" %(item[0], dayOfWeek[item[1]], item[2], item[3]))
		fp.close()


