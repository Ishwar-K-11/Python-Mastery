# In this code we are going to understand the different methods of dictionary

Marks = {
    "English": 89,
    "Hindi": 76,
    "Science": 91,
    "Math": 99,
    "SST": 81,
    "Geography": 91,
    "Python": 96,
}


# Calculating the total of the Marks avaible in the dictionary
total = 0
for sub in Marks.values():
    total += sub

print(total)
print(Marks.values())  # Only gives Values
print()
print()


# Keys Methods
for subs in Marks.keys():
    print(f"Subject = {subs} | Marks = {Marks[subs]}")

print(Marks.keys())  # Only gives Keys
print()
print()


# Printing the keys and values in the form of tuple or we can say together
print(Marks.items())

for details in Marks.items():
    print(details[0], details[1])


print()
for keys in Marks:  # Same as .keys()
    print(keys)
