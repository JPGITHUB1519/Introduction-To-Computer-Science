def pares(n):

    if(n % 2 == 0):

        return True
    else :
        return False

def imprimirpares():
    cont = 1
    while(cont <= 20):

        if pares(cont) == True:
            print cont
        cont = cont + 1

def sumapares():

    cont = 1
    suma = 0

    while(cont <= 20):

        if (pares(cont) == True):
            suma = suma + cont
        cont = cont + 1

    print "Suma : ", suma
