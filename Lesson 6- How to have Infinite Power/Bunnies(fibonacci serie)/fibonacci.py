# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    
    if(n == 0) :
        
        res = 0
        
    if(n == 1) :
        
        res = 1
    
    if n > 1 :
        
        res = fibonacci(n-1) + fibonacci(n-2)
    
    return res

print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610