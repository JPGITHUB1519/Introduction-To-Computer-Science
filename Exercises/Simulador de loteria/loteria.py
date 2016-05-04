from random import randint

def generar_premios(lista) :

	cont = 1

	while cont <= 3 :

		r = randint(1,100)
		lista.append(r)
		cont = cont + 1

def apostar(lista) :

	cont = 1


	print "\nCuantos numeros desea apostar : "
	cant = int(input())

	while cont <= cant :

		print "Ingrese #", cont, " : "
		n = int(input())

		lista.append(n)

		cont = cont + 1


def comprobar(premios, apuesta) :

	cont = 0
	cond = False

	while cont < len(apuesta) :

		if apuesta[cont] in premios :

				print "\nFelicidades, te sacaste con el numero ", apuesta[cont]
				cond = True
		cont = cont + 1


	if cond == False :

		print "\nNo has ganado"


	
def loteria() :

	apuesta = []
	apostar(apuesta)

	premios = []
	generar_premios(premios)

	print "\nPremios : ", premios
	comprobar(premios, apuesta)



loteria()
