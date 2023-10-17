sco = {'NAME': 'SCORE', 'fad': '14214'}
print('\tHigh Scores Keeper\n')
while True:
	print('\t0 - Quit')
	print('\t1 - List Scores')
	print('\t2 - Add a Score\n')
	cho = int(input('Choice: '))
	if cho == 0:
		break
	if cho == 1:
		d = sorted(sco.items(), key=lambda x: x[1], reverse=True)
		for key in sco:
			value = sco[key]
			print(key, value)
	if cho == 2:
		break		
