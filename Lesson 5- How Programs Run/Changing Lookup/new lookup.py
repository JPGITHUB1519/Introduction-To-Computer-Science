# Change the lookup procedure
# to now work with dictionaries.

ex = {"hola" : ["url1","url2"], "wiki" : ["url3","url4"]}

def lookup(index, keyword):

    if keyword in index :

    	return index[keyword]

    else :

    	return None

print ex

print lookup(ex, "wiki")

