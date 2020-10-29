"""Counting vowels"""

sentence = input ('introdusca un texto: ').lower()
voowels=0

for i in sentence:
	if i == 'a':
		voowels+=1
	elif i == 'e':
		voowels+=1
	elif i == 'i':
		voowels+=1
	elif i == 'o':
		voowels+=1
	elif i == 'u':
		voowels+=1
	
if voowels==0:
	print('no hay vocales en la oracion')
elif voowels ==1:
	print(f'hay {voowels} vocal' )
elif voowels >1:
	print(f'hay {voowels} vocales' )

