# we can find a string in a string
# <string>.find(<string>) -it give first position in search string where the targen string appear

word = "Python es un lenguaje de programacion interpretado cuya filosofia hace hincapie en una sintaxis que favorezca un codigo legible."

print word.find("lenguaje");

print word[13:]


print word.find("sintaxis")
print word[:86]

print word.find("Python")
print word[0:]


variable = word.find("interpretado")
print variable

print word[:37]

variable = word.find("thon")

print variable

print word [:variable]


