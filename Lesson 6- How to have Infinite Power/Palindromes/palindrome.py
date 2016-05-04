# Define a procedure is_palindrome, that takes as input a string, and returns a
# Boolean indicating if the input string is a palindrome.

# Base Case: '' => True
# Recursive Case: if first and last characters don't match => False
# if they do match, is the middle a palindrome?

cond = True
def is_palindrome(s):
    
    cond = False
    
    if(s == '') :
        cond = True
        return cond
    
    
    if s[0] != s[len(s)-1] :
        return False
    else :
        
        cond = is_palindrome(s[0+1:len(s)-1]);
    
    return cond
        
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True