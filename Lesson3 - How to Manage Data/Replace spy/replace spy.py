# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.


def replace_spy(list):

	list[2] = list[2] + 1


spy = [0,0,7]
replace_spy(spy)

print spy


# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.

#replace_spy(spy)
#print spy
#>>> [0,0,8]