from random import randint


def moneda() :

	r = randint(1,2)

	if r == 1 :

		return 1

	if r == 2 :

		return 2

cont = 1
cara = 0
cudo = 0


while cont <= 100 :

	moneda()
	if moneda() == 1 :
		cara = cara + 1
	else :

		cudo = cudo + 1

	cont = cont + 1

print cara
print cudo