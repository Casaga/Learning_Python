"""Burble method"""
import random 
num = int(input('cuantos numeros desea arreglar: '))
numbers=[]
for i in range(num):
	numbers.append(0)
for i in range(num):
	rar=0
	while rar==0:
		j=random.randint(0, num-1)
		if numbers[j]==0:
			numbers[j]=(i+1)
			rar=1
		else:
			rar=0
			
print(numbers)
deslist = numbers
rar=1
while rar!=0:
	rar=0
	for i in range(len(deslist)):
		if i!=len(deslist)-1:
			num1=deslist[i]
			num2=deslist[i+1]
			if num1 > num2 :
				deslist[i]=num2
				deslist[i+1]=num1
				rar=1
				print(deslist)

