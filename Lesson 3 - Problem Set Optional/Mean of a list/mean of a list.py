# The mean of a set of numbers is the sum of the numbers divided by the
# number of numbers. Write a procedure, list_mean, which takes a list of numbers
# as its input and return the mean of the numbers in the list.

# Hint: You will need to work out how to make your division into decimal
# division instead of integer division. You get decimal division if any of
# the numbers involved are decimals.

# check if a list if empty

#return False if a list is empty
def no_empty(lista):

	if len(lista) == 0 :

		return False

	return True

def list_mean(lista):

	if no_empty(lista) == False :

		return 0

	mean = 0.

	for i in lista :

		mean = mean + i

	mean = mean / len(lista)

	return mean




print list_mean([1,2,3,4])
#>>> 2.5
print list_mean([1,3,4,5,2])
#>>> 3.0
print list_mean([])
#>>> ??? You decide. If you decide it should give an error, comment
# out the print line above to prevent your code from being graded as
# incorrect.
print list_mean([2])
#>>> 2.0