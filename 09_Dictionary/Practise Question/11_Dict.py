"""
Construct a dictionary containing the names of six students and their respective marks.

Using a for loop:
1. Print the name and marks of each student.
2. Find the student who has scored the highest marks.
3. Display the name of the student along with the highest marks.

"""

students = {
    "Amit": 85,
    "Rahul": 92,
    "Sneha": 88,
    "Priya": 95,
    "Karan": 79,
    "Neha": 90
}
print("Student Marks")
print("__" * 20)

high_marks = 0
name_s = ""


for name, marks in students.items():
    print(f"{name} : {marks}")

    if marks > high_marks:
        high_marks = marks
        name_s = name

print("\nHighest Marks")
print("Name: ",name_s)
print("Marks: ",high_marks)
