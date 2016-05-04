# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.



def biggest (n1,n2,n3):

	if(n1 > n2 and n1 > n3 ):
		return n1

	if(n2 > n1 and n2 > n3):

			return n2

	if(n3 > n1 and n3 > n2):

			return n3
        
    if(n1 == n2 and n3 < n2):

		return n1

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)
#>>> 9