# Define a procedure, find_second, that takes
# two strings as its inputs: a search string
# and a target string. It should return a
# number that is the position of the second
# occurrence of the target string in the
# search string.




def find_second(search_string,target_string):

	first_appearance = search_string.find(target_string)

	return search_string.find(target_string, first_appearance+1)




danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')


twister = "she sells seashells by the seashore"
print find_second(twister,'she')
