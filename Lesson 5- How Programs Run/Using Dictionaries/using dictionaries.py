
#dictionary
#it is not i order

"""
Sintax

<name> = { "<key1>" : value1, "<key2>" :value2, "<keyn>" : valueN }

"""


elements = {"hydrogen" : 1, "helium" : 2, "carbon" : 6}

#<name>["key"]
print elements["hydrogen"]

#add new element
elements["calcium"] = 10

print elements["calcium"]

# guive an error print elements["nitrogen"]

#check if a value exits
print "nitrogen" in elements

