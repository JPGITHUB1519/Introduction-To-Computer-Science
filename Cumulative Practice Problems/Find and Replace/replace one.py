

def replace_string(string,match,replace) :

	pos =  string.find(match)
	final = pos + len(match)

	string = string[:pos] + replace + string[final:]

	return string



string = 'aaabaa'
match = 'aba'
replace = 'b'


#replace
print replace_string(string,match,replace)
