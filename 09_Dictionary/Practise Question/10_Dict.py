"""
Subject Peformace Analysis
    Given a dictionary of marks for different subjects, loop over its values() 
    to calculate and print the total of the marks and the average marks obtained.
"""

marks = {
    "Hindi" : 71,
    "English" : 78,
    "Science" : 91,
    "Math" : 98,
    "SST" : 84
}

total = 0
for mark in marks.values():
    total += mark

print("Total Marks Are : ",total)
percentage = (total / 5)
print(f"Percentage : {percentage}%")