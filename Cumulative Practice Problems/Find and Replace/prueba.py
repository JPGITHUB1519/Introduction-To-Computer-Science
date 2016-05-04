

def replace_string(string,match,replace) :

	pos =  string.find(match)

	string = string[:pos] + replace + string[len(match)+1:]

	return string



string = 'aaaba'
match = 'aba'
replace = 'b'


#replace
print replace_string(string,match,replace)