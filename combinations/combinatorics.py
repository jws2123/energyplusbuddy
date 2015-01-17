import csv
import itertools

## frange () is from 
def frange(start, end=None, inc=None):  #note: for quantitative variables needs to 
    "A range function, that does accept float increments..."

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
        labs.append([line['construction'], line['material'], line['variable']])
        seq.append(frange(float(line['lower']), float(line['upper']), float(line['stepsize'])))

combinations = list(itertools.product(*seq))

# save output.csv
with open('output.csv', 'wb') as file:
   	writer = csv.writer(file, delimiter=',')
	#temp placeholder for header
    	writer.writerow(['char1', 'char2', 'char3', 'char4'])
	
	for comb in combinations:
       		writer.writerow(comb)
            
print labs

# run idfBuddy
# for j, comb in enumerate(combinations):
#     for i, val in enumerate(comb):
#         print "idfBuddy '" + str(j) + ".idf' " + "'" + "' '".join(labs[i]) + "' " + "'" + str(val) + "'"