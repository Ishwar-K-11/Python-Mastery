# Sorting Dictionary in Dictionary using the lambda function

Students = {
    "student01": {"Math": 98, "English": 78, "Hindi": 79, "Science": 97},
    "student02": {"Math": 71, "English": 81, "Hindi": 62, "Science": 88},
    "student03": {"Math": 77, "English": 87, "Hindi": 69, "Science": 98},
    "student04": {"Math": 89, "English": 61, "Hindi": 77, "Science": 71},
}

ans = dict(sorted(Students.items(), key=lambda x: x[1]["Math"]))
print(
    ans
)  # Sorted the list according to the math marks no matter what is infront of it


# ans = dict(sorted(Students.items(), key=lambda x: x[1]["Math"] +x[1]["English"] +x[1]["Hindi"] +x[1]["Science"]))
# Now it will sort the dictionary according to the total addition of the marks 


