lista = [[1,2,3,4],
        [2,3,1,3],
        [3,1,2,3],
        [4,4,4,4]]



cons = 0
li = 0
aux = []
convertida = []

while cons < len (lista) : 

		while li < len(lista) :

			aux.append(lista[li][cons])
			li = li + 1

		li = 0
		cons = cons + 1
		convertida.append(aux)
		aux = []
print convertida



		

