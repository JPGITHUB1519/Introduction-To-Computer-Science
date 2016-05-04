lista = [1]

aux = []

aux.append(1)


while(cont <= n) :
	i = 0
	while(i < len(lista)-1) :

		aux.append(lista[i] + lista[i+1])

		i = i + 1

	aux.append(1)
	n = n + 1
	lista.append([aux])
	aux = []

print lista

