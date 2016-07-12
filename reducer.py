import fileinput

indexidMacchina = 0
indexTempo = 1
mr = {}

for line in fileinput.input():
	if(line.strip()):
		values = line.split('\t')
		idMacchina = str(values[indexidMacchina])
		tempo = float(values[indexTempo])
		temp = {str(idMacchina) : tempo}
		if idMacchina in mr.keys():
			mr[idMacchina] = mr[idMacchina] + tempo
		else:
			mr.update(temp)

print(mr)