# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    hash_table = []
    i = 0
    while i < nbuckets :
        hash_table.append([])
        i = i + 1
    
    return hash_table


lista = make_hashtable(1)
print lista





