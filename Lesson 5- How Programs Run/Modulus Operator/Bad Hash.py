def bad_hash(keyword, buckets) :

	return ord(keyword[0]) % buckets


print bad_hash("s", 1)

lista =  map(chr,range(97,123))

for x in lista :

	print bad_hash(x,100)
