def test_hash_function(func, keys, size):
   results = [0] * size  #this makes a list where all elements refer to same thing(0)
   keys_used = []
   for w in keys:
       if w not in keys_used:
           hv = func(w, size)
           results[hv] += 1
           keys_used.append(w)
   return results

words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split() # initialize all the words from the page 'Adventures of Sherlock Holmes'
counts = test_hash_function(bad_hash_string, words, 12) # obtain the counts for the old string
print counts
[725, 1509, 1066, 1622, 1764, 834, 1457, 2065, 1398, 750, 1045, 935]
counts = test_hash_function(hash_string, words, 12) # find the distribution for the new function
[1363, 1235, 1252, 1257, 1285, 1256, 1219, 1252, 1290, 1241, 1217, 1303]