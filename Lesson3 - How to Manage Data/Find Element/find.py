# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(lista,target) :

	cont = 0
	cond = False

	for i in lista :

		if i == target :

			return cont
			cond = True

		cont = cont + 1 

	if cond == False :

		return - 1


print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1