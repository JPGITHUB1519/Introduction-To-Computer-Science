lista = [[1,2,3],
		 [4,5,6],
		 [7,8,9],
		 ]


x = 0 
y = 0

while x < len(lista) :

	while y < len(lista) :

		lista[x][y] = lista[y][x]
		y = y+ 1
		x = x + 1

print lista