# Creating a clss and its object

class Student:
    name = ""
    roll_no = 0
    stream = ""
    gender = ""
    marks = 0
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Stream or School: {self.stream}")
        print(f"Roll Number: {self.roll_no}")
        print(f"The Gender of student: {self.gender}")
        print(f"Total Marks Obtained By the Student: {self.marks}")


student_1 = Student()

# Assign the values for the varibles in the class
student_1.name = "Mike Hussy"
student_1.roll_no = 55
student_1.stream = "B.Tech - CSE"
student_1.marks = 88
student_1.gender = "Male"

student_1.display()





