"""Alphabetic Substring"""
text = input ('introdusca un texto: ').lower()
flag=0;
iini=0
ifin=0
maxnumber=0
maxiini=0
maxifin=0

for i in range(len(text)):

	cha=ord(text[i])

	if cha>flag:
		flag=cha

	else: 
		ifin=i-1
		flag=cha
		if (ifin-iini)>maxnumber:
			maxnumber=ifin-iini
			maxifin=ifin
			maxiini=iini
			iini=i
			

	if i==len(text)-1:
		if (len(text)-1-iini)>maxnumber:
			maxnumber=len(text)-1-iini
			maxifin=len(text)-1
			maxiini=iini


world=['']
for j in range(maxiini,maxifin):			
	world.append(text[j])
	print(world)

text2=''.join(world)
print(f'la secuencia de palabras mas larga encontrada fue: {text2}')