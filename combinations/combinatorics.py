import csv
import itertools
import os

def frange(start, end=None, inc=None):
    if end == None:
        end = start + 0.0
        start = 0.0

    if inc == None:
        inc = 1.0

    L = []
    while 1:
        next = start + len(L) * inc
        if inc > 0 and next > end:
            break
        elif inc < 0 and next <= end:
            break
        L.append(next)
        
    return L

seq = []
labs = []
with open('changes.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        labs.append([line['material'], line['variable']])
        seq.append(frange(float(line['lower']), float(line['upper']), float(line['stepsize'])))

combinations = list(itertools.product(*seq))

# save output.csv
header = []            
for i,h in enumerate(labs):
    header.append('-'.join(h))

with open('output.csv', 'wb') as file:
   	writer = csv.writer(file, delimiter=',')
	#temp placeholder for header
    	writer.writerow(header)
	
	for comb in combinations:
       		writer.writerow(comb)

# run idfBuddy
for j, comb in enumerate(combinations):
    os.system("cp ./idfs/template.idf ./idfs/" + str(j) + ".idf")
    for i, val in enumerate(comb):
        os.system("python ../idfBuddy/idfBuddy.py '" + "./idfs/" + str(j) + ".idf' " + "'" + "' '".join(labs[i]) + "' " + "'" + str(val) + "'")
