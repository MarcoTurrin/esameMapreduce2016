import fileinput

indexidMacchina = 2
indexTempo = 3

for line in fileinput.input():
	values = line.split(';')
	idMacchina = values[indexidMacchina ]
	tempo = values[indexTempo]
	print('{0}\t{1}'.format(idMacchina, tempo))