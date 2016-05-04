
elements = {}
#dictionaries intro dictionary
#we can any value in a dictionary

elements["H"] = {"name" : "Hydrogen", "number" : 1, "weight" : 1.00794}
elements["HE"] = {"name" : "Helium" , "number" : 2 , "weight" : 4.0022602, "noble gas" : True}

print elements["H"]

print elements["H"]["name"]
print elements["H"]["weight"]
print elements["HE"]["name"]
print elements["HE"]["noble gas"]