# Create a Dictionary contains mark of scored by a student in various subjects.
# Print the Dictionary 
# Also Update the Marks Of one Subject

Sam_Marks = {
    "English" : 89,
    "Hindi" : 76,
    "Science" : 91,
    "Math" : 99,
    "SST" : 81,
    "Geography" : 91,
    "Python" : 96
}

print(Sam_Marks)                     # Printing The Entire Dictionary 
print(Sam_Marks["Science"])          # Prints the Marks of science

print(id(Sam_Marks))  #id() returns the unique identity (memory address) of an object during its lifetime.
