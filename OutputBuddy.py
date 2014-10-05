import os
import sys

count = 0
for (dirname, dirs, files) in os.walk('/Output'):
	for filename in files:
		if filename.endswith(".csv"):
			count = count + 1

for files in range(0,count):
	
	f = open(str(files+1) + ".csv", "r")
	output = open("output.csv", "w")
	
	





