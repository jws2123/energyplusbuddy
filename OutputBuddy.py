import os
import sys

count = 0
for (dirname, dirs, files) in os.walk('/Output'):
	for filename in files:
		if filename.endswith(".csv"):
			count = count + 1

f = open(str("1.csv", "r")
output = open("output.csv", "a")
#f.readline

#output.append(

#probably going to need to re-write this with pandas... not sure if you can append one line at a time the way we need to.

for files in range(0,count):
	
	f = open(str(files+1) + ".csv", "r")
	output = open("output.csv", "a")
	
	

	for line in f:
		if line == (files+1) :
			output.append("," + line) 





