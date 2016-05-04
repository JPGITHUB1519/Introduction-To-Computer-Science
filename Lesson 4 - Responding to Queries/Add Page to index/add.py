# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword):

	for i in index :

		if i[0] == keyword :

			return i[1]

	return []

def add_page_to_index(index,url,content):

	aux = content.split()

	for i in aux :

		#index.append([i,[url]]);
		add_to_index(index,i,url)


add_page_to_index(index,'fake.text',"This is a test")
add_page_to_index(index,"prueba.test","is a")

print index

print lookup(index,"a")

#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]



