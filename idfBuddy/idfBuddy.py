import sys
import os
#import time

file = sys.argv[1]
material = sys.argv[2]
variable = sys.argv[3]
var_value = sys.argv[4]
found_material_definition = False
found_material = False
found_variable = False

split = file.split(".")
split[-2] = split[-2]+"_temp"
newfile = '.'.join(split)

print newfile
				
new_f = open(newfile, 'w+')

with open(file) as f:
	for line in f:
		temp_line = line.strip()
		temp_line = temp_line.upper()
		if found_material:
			variable = variable.upper()
			if variable in temp_line:
				split = line.split(",")
				split[0] = "  " + var_value
				line = ",".join(split)
			if ";" in temp_line:
				found_material = False		
		if found_material_definition:
			material = material.strip()
			material = material.upper()
			if material in temp_line:
				found_material = True
			found_material_definition = False
		else:
			if temp_line == "MATERIAL," or temp_line == "WINDOWMATERIAL:GLAZING,":
				found_material_definition = True
		new_f.write(line)

new_f.close()

os.system("mv " + newfile + " " + file)

