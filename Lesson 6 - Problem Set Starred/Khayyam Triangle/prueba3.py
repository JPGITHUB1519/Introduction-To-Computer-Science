
lista = [[1]
aux = []
aux.append(1)
i = 0
while(i < len(lista[-1])) :
            
    aux.append(lista[len(lista[-1])][i] + lista[len(lista[-1])][i+1])

    i = i + 1

    aux.append(1)
    lista.append(aux)

print lista
