from random import randint


def moneda() :

	r = randint(1,2)

	if r == 1 :

		print "\nCara"

	if r == 2 :

		print "\nCudo"


moneda()