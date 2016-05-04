p = ["h", "e", "l", "l", "o"]

p[0] = "y"

# we asign a the same objet that refers p
a = p

a[4] = "!"

#the value of p changes too, though we do not change the value of p.
# it is because a and p refers to the object


print a 
print p

