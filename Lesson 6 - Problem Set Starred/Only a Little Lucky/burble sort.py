diccionario = {"b" :2, "d" : 4,"c" : 3,"a" : 1}

lista = []

for clave, valor in diccionario.iteritems(): 
    
    lista.append([clave,valor])
    
i = 0
j = 0
while i < len(lista) :
    while j < len(lista) - 1 :
        if lista[j][1] < lista[j+1][1] :
            aux = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = aux
            
            
        j = j + 1
    j = 0        
    i = i + 1


print lista

	

	


	
