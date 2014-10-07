import os
import sys
import pandas as pd


output = pd.read_csv("../combinations/output.csv")

location = "/output"

count = 0
for (dirname, dirs, files) in os.walk(location):
	for filename in files:
		if filename.endswith(".csv"):
			count = count + 1

f = open("output/1.csv")
columns = f.readline
f.close()

index=range(0,count)

#creating an empty dataframe
results_compiled = DataFrame(index=index, columns=columns)

for i in index:
	df = pd.read_csv("location/" + str(i) + ".csv")
	transpose = df.T
	
	

#f = open(str("1.csv", "r")
#output = open("output.csv", "a")
#f.readline

#output.append(

#probably going to need to re-write this with pandas... not sure if you can append one line at a time the way we need to.

#for files in range(0,count):
	
#	f = open(str(files+1) + ".csv", "r")
#	output = open("output.csv", "a")
	
	

#	for line in f:
#		if line == (files+1) :
#			output.append("," + line) 





