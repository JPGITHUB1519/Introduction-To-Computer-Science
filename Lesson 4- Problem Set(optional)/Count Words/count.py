# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.

def count_words(words):
    
    #one because when it starts in is one word
    
    if len(words) == 0 :
        
        return 0
    
    cant = 1
    x = 0
    while x < len(words) :
        if words[x] == " " :
            cant = cant + 1
        x = x + 1
    return cant



passage =("The number of orderings of the 52 cards in a deck of cards "
"is so great that if every one of the almost 7 billion people alive "
"today dealt one ordering of the cards per second, it would take "
"2.5 * 10**40 times the age of the universe to order the cards in every "
"possible way.")
print count_words(passage)

#>>>56

