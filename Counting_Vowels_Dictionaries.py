"""Counting Vowels with dictionaries"""
sentence = input ('introdusca un texto: ').lower()
Vowels_Dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}

for l in sentence:
	if l == 'a':
		Vowels_Dict['a']+=1
	elif l == 'e':
		Vowels_Dict['e']+=1
	elif l == 'i':
		Vowels_Dict['i']+=1
	elif l == 'o':
		Vowels_Dict['o']+=1
	elif l == 'u':
		Vowels_Dict['u']+=1

print(f'hay' ,Vowels_Dict['a'], 'a')
print(f'hay' ,Vowels_Dict['e'], 'e')
print(f'hay' ,Vowels_Dict['i'], 'i')
print(f'hay' ,Vowels_Dict['o'], 'o')
print(f'hay' ,Vowels_Dict['u'], 'u')