
def convert(string, struct) :

	new_string = ""

	for i in range(0, len(string)) :

		if i == len(string)-1 :

			aux = string[i-1] + string[i] + string[0]
		else :
			aux = string[i-1] + string[i] + string[i+1]

		new_string = new_string + struct[aux]

	return new_string