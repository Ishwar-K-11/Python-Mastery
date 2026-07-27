# create a dictionary and peform the various operation of membership Operators

Info = {
    "Name" : "Jack",
    "Age" : 39,
    "City" : "Delhi",
    "Country" : "India"
}

print("Age" in Info)           # Checks if the Key exist in the Dictionary if yes print True if not print False

print("Mobile" not in Info)    # Prints True if not exist in the Dictionary

print("Jack" in Info.values()) # Check the value is present or not

print(("Name", "Jack") in Info.values()) # Check multiple items is present or not