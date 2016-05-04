# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def convert_row(lista) :
  cons = 0
  li = 0
  aux = []
  convertida = []

  while cons < len (lista) : 

     while li < len(lista) :

        aux.append(lista[li][cons])
        li = li + 1

     li = 0
     cons = cons + 1
     convertida.append(aux)
     aux = []

  return convertida

#check if the lists of the list has the seim len
# retur False if is not
def check_len(lista):

	tam = len(lista[0])

	for i in lista :

		if len(i) != tam :

			return False

	return True

# Check if a list is empty
# return False if is empty
def no_empty(lista) :

	if len(lista) == 0 :

		return False

def symmetric(lista):
    # Your code here

    if no_empty(lista) == False :

    	return True

    if check_len(lista) == False :

    	return False

    if lista == convert_row(lista) :

    	return True

    else :

    	return False



print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "fish"],
#                ["fish", "fish", "cat"]])
#>>> True

#print symmetric([["cat", "dog", "fish"],
#                ["dog", "dog", "dog"],
#                ["fish","fish","cat"]])
#>>> False

#print symmetric([[1, 2],
#                [2, 1]])
#>>> True

#print symmetric([[1, 2, 3, 4],
#                [2, 3, 4, 5],
#                [3, 4, 5, 6]])
#>>> False

#print symmetric([[1,2,3],
#                 [2,3,1]])
#>>> False