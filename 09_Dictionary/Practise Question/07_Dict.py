"""
Q Safe Subject Acess
    Define a dictionary with the five subjects and their respective marks. 
    Unlike the get() methods to by acessing a subject that is not in the dictionary ensuring it "prints not avaible" as default 
"""

marks = {
    "English": 85,
    "Mathematics": 92,
    "Science": 88,
    "History": 79,
    "Computer": 95
}

print("English    :", marks.get("English", "Not Available"))
print("Mathematics:", marks.get("Mathematics", "Not Available"))
print("Science    :", marks.get("Science", "Not Available"))
print("History    :", marks.get("History", "Not Available"))
print("Computer   :", marks.get("Computer", "Not Available"))

# Accessing a subject that does not exist
print("Geography  :", marks.get("Geography", "Not Available"))

"""
Lets understand what the answer says
    from the line print("English    :", marks.get("English", "Not Available"))
        frist as the text in the output we print the English : 
        and in the marks.get("English", "Not Available")
            so the inside the get it cheks the key English and its value is avaible or not if yes print or not print the not avaible message

            
and in subject that does not exists it says that .get method checks the geography exists or not if not then print the simple message not avaible

"""