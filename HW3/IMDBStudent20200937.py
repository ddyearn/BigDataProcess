#!/usr/bin/python3

import sys

with open(sys.argv[1], "rt") as f:
	data = f.read()

jpm = []
jenres = {}

rows = data.split("\n")
for row in rows:
	info = row.split("::")
	jpm.append(info[2])

for m in jpm:
	jenre = m.split("|")
	for j in jenre:
		if j in jenres:
			jenres[j] += 1
		else:
			jenres[j] = 1

with open(sys.argv[2], "wt") as fp:
	for js in jenres:
		fp.write("%s %d\n" % (js, jenres[js]))


