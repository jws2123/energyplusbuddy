import os
import sys
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt


output = pd.read_csv("../combinations/output.csv")

outputFileLocation = "output"

count = 0
for (dirname, dirs, files) in os.walk(outputFileLocation):
	for filename in files:
		if filename.endswith(".csv"):
			count = count + 1

df = pd.read_csv(outputFileLocation + "/1.csv")

index=range(2,count+1)

for i in index:
	tempDf = pd.read_csv(outputFileLocation + "/" + str(i) + ".csv")
	df = df.append(tempDf.iloc[0])

print df
	


