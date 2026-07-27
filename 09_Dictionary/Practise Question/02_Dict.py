""" 
Create a list of MArks of Student of different Subjects And Prform the following operations
    1) Add one subject with its marks
    2) Upade the marks of subject SST

"""

Sam_Marks = {
    "English" : 89,
    "Hindi" : 76,
    "Science" : 91,
    "Math" : 99,
    "SST" : 81,
    "Geography" : 91,
    "Python" : 96
}
# Adding key and its value to the Dictionary
Sam_Marks["Java"] = 69

# What if you want to add multiple keys and its value the simple use the .update() methode
Sam_Marks.update({"BEE" : 97, "BXE" : 61})


# Updating the marks Of SST Subject
Sam_Marks["SST"] = 87




# The following line will check if the key exits and if exists it will update and if not the add key and its value
Sam_Marks["C++"] = 76

print(Sam_Marks)


# What if you two keys with the name SST and different values. So python will keep the leatest or last
# key and its value but the order will be the frist apperence
# Example
Info = {
    "Name" : "Sam",
    "Age" : 33,
    "City" : "Mumbai",
    "Age" : 88
}
print(Info)