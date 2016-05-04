# Question 9: Deep Reverse
# Define a procedure, deep_reverse, that takes as input a list, 
# and returns a new list that is the deep reverse of the input list.  
# This means it reverses all the elements in the list, and if any 
# of those elements are lists themselves, reverses all the elements 
# in the inner list, all the way down. 

# Note: The procedure must not change the input list.

# The procedure is_list below is from Homework 6. It returns True if 
# p is a list and False if it is not.

def is_list(p):
    return isinstance(p, list)

def reverse_list(lista):
    aux_lista = []
    cont = len(lista) - 1
    
    while cont >= 0 :
        if is_list(lista[cont]) :
            aux_lista.append(reverse_list(lista[cont]))
        else :
            aux_lista.append(lista[cont])
        
        

        
        cont = cont - 1
        
    return aux_lista

def deep_reverse(lista):
    aux_lista = []
    cont = len(lista) - 1
    while cont >= 0 :
        if is_list(lista[cont]) :
            aux_lista.append(reverse_list(lista[cont]))
        else :
            aux_lista.append(lista[cont])
        
        cont = cont - 1
        
    return aux_lista
   


#For example,

p = [1, [2, 3, [4, [5, 6]]]]
print deep_reverse(p)
#>>> [[[[6, 5], 4], 3, 2], 1]
print p
#>>> [1, [2, 3, [4, [5, 6]]]]

q =  [1, [2,3], 4, [5,6]]
print deep_reverse(q)
#>>> [ [6,5], 4, [3, 2], 1]
print q
#>>> [1, [2,3], 4, [5,6]]
