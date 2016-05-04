
#find the two things in one procedure
def connections_and_likes(string) :

    #1 - for connections
    #2 -  for likes
    #3 - for users

    struct = {}
    connection_find = "is connected to"
    likes_find = "likes to play"
    pos_connections = 0  
    pos_likes = 0 
    aux_connection = ""
    aux_likes = ""
    find_point = 0
    find_point2 = 0
    #for connections
    lista = []
    #for likes
    lista2 = []

    #for users
    lista3 = []
    cond = True
   
    while True :
        pos_comma = 0
        pos_comma2 = 0
        sublista = []
        sublista2 = []
       
        pos_connections = string.find(connection_find)
        pos_likes = string.find(likes_find)
        if pos_connections == - 1 or pos_likes == - 1 :
            break


        find_point = string.find(".")
        find_point2 = string.find(".", string.find(".") + 1 )

       
        aux_connection = string[pos_connections + len(connection_find) + 1 : find_point]
        aux_likes = string[pos_likes + len(likes_find) + 1 : find_point2]
    
        while True :

            pos_comma = aux_connection.find(",")
            pos_comma2 = aux_likes.find(",")

            if pos_comma == -1 or pos_comma2 == - 1 :

                break
            sublista.append(aux_connection[:pos_comma])
            sublista2.append(aux_likes[:pos_comma2])
            aux_connection = aux_connection[pos_comma + 2 :]
            aux_likes = aux_likes[pos_comma2 + 2 :]

        sublista.append(aux_connection[0 : ])
        sublista2.append(aux_likes[0 : ])

        lista.append(sublista)
        lista2.append(sublista2)
       
        find_point = string.find(".", find_point + 1 )
        string = string[find_point + 1:]  
    return lista, lista2   



example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


lista, lista2 = connections_and_likes(example_input)

print lista
print lista2