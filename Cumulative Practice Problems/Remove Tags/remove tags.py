# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(string):
    lista = []
    
    cond = string.find("<")
    
    if cond == -1 :
        
        return string.split()
    
    if string[0] != "<" :
        
            lista = string[:cond].split()
    string = string[cond:]
    
    first = 0
    second = 0
    
 
    while first != -1 :
        
        first = string.find("<")
        
        if first == - 1 :
            
            aux = string.split()
            
            for i in aux :
                
                lista.append(i)
            

        second = string.find(">")
       
        third = string.find("<", first + 1)
        
        if third != - 1 :
            if string[second+1 : third] != '' :
                
                aux = string[second+1 : third].split()
                
                for i in aux :
                
                    lista.append(i)
                
                #lista.append(string[second+1 : third].split())
                #lista.append(string[second+1 : third].split())
            
        
            
        string = string[second + 1:]
        
    return lista


print remove_tags('''<start>This line starts and ends with a tag<end>''')
print remove_tags('''<br />This line starts with a tag''')
print remove_tags('''This is in <i>italics</i>''')
print remove_tags('''<h1>A</h1><p>hola</p>''')

print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                     <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']