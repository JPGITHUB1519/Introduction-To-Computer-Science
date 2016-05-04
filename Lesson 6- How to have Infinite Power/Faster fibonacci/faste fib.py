#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    
    ant = 0
    desp = 1
    aux = 0
    
    while(n > 1) :
        
        aux = ant
        ant = desp
        desp = aux + desp
        
        n = n - 1
    
    return desp
        
print fibonacci(7)
#print fibonacci(36)
#>>> 14930352