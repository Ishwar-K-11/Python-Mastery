students = {
    "Aarav": {
        "English": 85,
        "Math": 92,
        "Science": 88,
        "History": 90,
        "Computer": 95
    },

    "Bhavya": {
        "English": 78,
        "Math": 85,
        "Science": 80,
        "History": 82,
        "Computer": 84
    },

    "Charan": {
        "English": 91,
        "Math": 89,
        "Science": 94,
        "History": 93,
        "Computer": 96
    },

    "Diya": {
        "English": 88,
        "Math": 90,
        "Science": 87,
        "History": 89,
        "Computer": 91
    },

    "Eshan": {
        "English": 80,
        "Math": 79,
        "Science": 85,
        "History": 81,
        "Computer": 83
    }
}

topper = ""
highest_avg = 0

for student, marks in students.items():
    average = sum(marks.values()) / len(marks)

    print(f"{student} Average = {average:.2f}")

    if average > highest_avg:
        highest_avg = average
        topper = student

print("\nTopper:", topper)
print("Highest Average:", round(highest_avg, 2))