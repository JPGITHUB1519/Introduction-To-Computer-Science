

def find(lista,target) :


	cont = 0
	while cont < len (lista)  :

		if lista[cont] == target :

			return cont

		cont = cont + 1

	return - 1

print find([1,2,3],3)
#>>> 2

print find(['alpha','beta'],'gamma')
#>>> -1

