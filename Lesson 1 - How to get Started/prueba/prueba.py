
from random import randint

opciones = ["casa", "perro","oso","nave","avion"]

def generar_palabra(opciones) :


    r = randint(0,len(opciones)-1)

    palabra = opciones[r]


    return palabra

def generar_vidas() :

    r = randint(5,10)

    return r

def tip(palabra) :

    if palabra[0] == "c" :

        print "\nLa palabra empieza con c "

    if palabra[0] == "a" :

        print "\nLa palabra empieza con a"

    if palabra[0] == "o" :

        print "\nLa palabra empieza con o"

    if palabra[0] == "p" :

        print "\nLa Palabra empieza con p"

    if palabra[0] == "n" :

        print "\nLa palabra empieza con n"


    print "\nCantidad de letras : ", len(palabra)


def jugar() :

    print "\t\t\tJuego Adivinar Palabra"

    word = generar_palabra(opciones)
    vidas = generar_vidas()
    tip(word)

    while vidas > 0 :

        print "\nNumero de vidas : ",vidas

        print "\nIngrese la palabra : "
        opcion = raw_input()

        if opcion == word :

            print "\nFelicidades!!!!!, has adivinado la palabra"
            break

        else :

            vidas = vidas - 1
            print "\nLo siento, has fallado......."
            print "\nTe quedan ", vidas, " Vidas"
            if vidas == 0 :
                print "\nGAME OVER"




jugar()


