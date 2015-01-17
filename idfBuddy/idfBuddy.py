import sys

#print "\n".join(sys.argv[1:])

file = sys.argv[1]
material = sys.argv[2]
variable = sys.argv[3]
var_value = sys.argv[4]

with open(file) as f:
	for line in f:
		line = line.strip()
		line = line.upper()
		material = material.upper()
		if line == material:
			print line
		##else: 
		##	print 0

