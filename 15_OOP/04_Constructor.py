"""
==============================
Constructor (__init__)
==============================

Definition:
    A constructor is a special method in a class that is automatically called whenever an object of the class is created. It is used to initialize the object's attributes.

Syntax:
    class ClassName:
        def __init__(self, parameters):
            # Initialize attributes

Example:

    class Student:
        def __init__(self, name, roll):
            self.name = name
            self.roll = roll

    student1 = Student("Ishwar", 101)

    print(student1.name)
    print(student1.roll)

Output:
    Ishwar
    101
"""


class Student():
    def __init__(self,n:str,s:str,r:int,g:str,m:int) -> None:
        self.name = n
        self.school = s
        self.roll = r
        self.gender = g
        self.mark = m

    def display(self):
        print(self.name)
        print(self.school)
        print(self.roll)
        print(self.gender)
        print(self.mark)

student1 = Student("Jack","SOE&T",20,"Male",70)
student1.display()



#init methos overcomes the Attribute Error