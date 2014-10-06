import csv

for i in range(0,7985):
	with open (str(i) + ".csv", "wb") as file:
		writer = csv.writer(file, delimiter=',')
		writer.writerow(["energy_output1", "energy_output2", "energy_output3", "energy_output4"])
		writer.writerow([0,0,0,0])

