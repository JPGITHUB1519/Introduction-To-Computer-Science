def getcomponents(n) :

	elements = []

	if n >= 128 :

		n = n - 128
		elements.append(128)

	if n >= 64 :

		n = n - 64
		elements.append(64)

	if n >= 32 :

		n = n - 32
		elements.append(32)

	if n >= 16:

		n = n - 16
		elements.append(16)

	if n >= 8 :

		n = n - 8
		elements.append(8)

	if n >= 4 :

		n = n - 4
		elements.append(4)

	if n >= 2 :

		n = n - 2
		elements.append(2)

	if n >= 1 :
		n = n - 1
		elements.append(1)


	return elements

n = 142

print getcomponents(n)