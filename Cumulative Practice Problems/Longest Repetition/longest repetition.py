# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(lista):


	if len(lista) == 0 :

		return None

	else :

		objecto = lista[0]
		maxi = 1
		cont = 1

		
		for i in range(1,len(lista)):

			if lista[i] != lista[i-1] :	
				cont = 1
			else :
				cont = cont + 1
				if cont > maxi :
					maxi = cont
					objecto = lista[i-1]

		return objecto

			
#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

print longest_repetition([2, 2, 3, 3, 3])

