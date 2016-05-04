
def fill_connections(string) :
    struct = {}
    connection_find = "is connected to"
    pos_connections = 0
    aux_connection = ""
    find_point = 0
    lista = []
    while True :
        pos_connections = string.find(connection_find)
        if pos_connections == - 1 :
            break
        find_point = string.find(".")
        aux_connection = string[pos_connections + len(connection_find) + 1 : find_point]
        print aux_connection
        find_point = string.find(".", find_point + 1 )
        string = string[find_point + 1:]  


#in list
def fill_connections2(string) :
    struct = {}
    connection_find = "is connected to"
    pos_connections = 0
    aux_connection = ""
    find_point = 0
    lista = []
    cond = True
   
    while True :
        pos_comma = 0
        sublista = []
       
        pos_connections = string.find(connection_find)
        if pos_connections == - 1 :
            break


        find_point = string.find(".")
       
        aux_connection = string[pos_connections + len(connection_find) + 1 : find_point]
    
        while True :

            pos_comma = aux_connection.find(",")

            if pos_comma == -1 :

                break
            sublista.append(aux_connection[:pos_comma])
            aux_connection = aux_connection[pos_comma + 2 :]

        sublista.append(aux_connection[0 : ])

        lista.append(sublista)
       
        find_point = string.find(".", find_point + 1 )
        string = string[find_point + 1:]  
    return lista       
        
        
	
 
        

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


print fill_connections2(example_input)