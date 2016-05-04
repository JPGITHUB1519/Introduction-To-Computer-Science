
lista = [2,2,3]
cond = True

aux = []

for i in lista :

	if i not in aux :

		aux.append(i)

if len(aux) < 3 :

	cond = False

print cond
