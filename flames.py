def FLAMES(name1, name2):

	name1 = name1.replace(' ', '').lower()
	name2 = name2.replace(' ', '').lower()

	for i in name1.strip().lower():
		for j in name2.lower():
			if i == j:
				name1 = name1.replace(i, '')
				name2 = name2.replace(j, '')

	count = len(name1) + len(name2)

	flames = ['f', 'l', 'a', 'm', 'e', 's']

	if count == 0:
		return print('No compatibility')

	while len(flames) > 1:
		
		cutindex = count - len(flames)
		cutindex = cutindex - 1
		
		while cutindex > len(flames)-1:
			cutindex = cutindex - len(flames)

		flames.pop(cutindex)

	flames_dict = {'f': 'friend', 'l': 'love', 'a': 'affection', 'm': 'marriage', 'e': 'enemy', 's':'sister'}

	return print(' compatibility between name1 and name 2 is ', flames_dict[flames[0]].upper())

name1 = input('Enter your name1: ')
name2 = input('Enter your name2 : ')

FLAMES(name1, name2)