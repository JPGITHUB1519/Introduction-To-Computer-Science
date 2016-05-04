

def replace_string(string,match,replace) :
    
    pos = 0
    
    while True :
        pos =  string.find(match)
        if pos == - 1 :
            break
        final = pos + len(match)

        string = string[:pos] + replace + string[final:]

    return string



string = 'aaabaa'
match = 'aba'
replace = 'b'


#replace
print replace_string(string,match,replace)
