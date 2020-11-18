"""number tower"""
number=int(input ("introduzaca un numero: "))
for i in range(number+1):
	file=['']
	for j in range(i):
		file.append(f'{i}')
	print(''.join(file))

for i in range(number-1,0,-1):
	file=['']
	for j in range(i):
		file.append(f'{i}')
	print(''.join(file))