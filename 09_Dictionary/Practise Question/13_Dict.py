dict_in_dict = {
    "101" : {"Name" : "Ayush", "Age" : 18, "Sex" : "Male"},
    "102" : {"Name" : "Jack", "Age" : 20, "Sex" : "Female"},
    "103" : {"Name" : "Chandan", "Age" : 25, "Sex" : "Male"},
    "104" : {"Name" : "Sam", "Age" : 27, "Sex" : "Female"},

}

print(dict_in_dict["101"]["Name"])

for roll_no, details in dict_in_dict.items():
    print(f"Roll No: {roll_no} Name: {details['Name']}")

# So in the sbove code you will se that in roll_no store the details of all the keys of dict_in_dict dictionary
# and the details store the dictionarys associated with the roll no
# so details['Name'] here the details try to acess the dict and the Name is the key of the second dictionary
