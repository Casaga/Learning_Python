"""calculate the utopian tree"""
trees = int(input('numero de arboles a testear: '))
woods=0
for i in range(trees):
		cycles=int(input(f'cyclos del arbol {i+1}: '))
		wood=1
		while (cycles != 0 or cycles>0): 
			if cycles%2:
				wood*=2
			else:
				wood+=1
			cycles-=1
		woods+=wood
		print(f'el arbol crecio {wood} metros')
print(f'el total de madera que se obtuvo es {woods} metros')