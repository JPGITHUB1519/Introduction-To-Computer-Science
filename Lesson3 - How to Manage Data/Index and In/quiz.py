# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(lista,target) : 

	if target in lista :

		return lista.index(target)
	else :

		return -1

def find2_element(lista,target) :

	if target not in lista :

		return -1

	else :

		return lista.index(target)



print find_element([1,2,3],3)
#>>> 2print find_element([1,2,3],3)

print find_element(['alpha','beta'],'gamma')
#>>> -1

print find2_element([1,2,3],3)