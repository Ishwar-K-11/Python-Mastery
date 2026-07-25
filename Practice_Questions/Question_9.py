# Take a student's mark as input Print their garde based on this scale:
# 90 and above: A
# 75 to 89: B
# 60 to 74: C
# 40-59: D
# Below 40: F

mark = int(input("Enter the student's mark: "))

if mark >= 90:
    print("Grade: A")
elif mark >= 75:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
elif mark >= 40:
    print("Grade: D")
else:
    print("Grade: F")