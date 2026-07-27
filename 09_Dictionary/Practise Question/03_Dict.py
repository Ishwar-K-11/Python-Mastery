# Create a Dictionary And Try to Delete the items from the dictionary in all the possible ways

Marks = {
    "English" : 89,
    "Hindi" : 76,
    "Science" : 91,
    "Math" : 99,
    "SST" : 81,
    "Geography" : 91,
    "Python" : 96
}

print(id(Marks))

Marks.pop("Math")       # Removes the Key and its Value from the Dictionary by the key value name  

print(Marks)

Marks.clear()           #  Removes every things inside the dictionary (Makes the Dict Empty) 

print(Marks)

del Marks["Python"]     # Removes key python From The Dictonary
del Marks               # This deletes the entire Dictionary with the varible 

