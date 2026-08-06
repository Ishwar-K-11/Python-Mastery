"""
==============================
Getter and Setter Methods
==============================

Getter Method:
--------------
A getter method is used to access (read) the value of a private attribute.

Syntax:
    def get_attribute(self):
        return self.__attribute

Setter Method:
--------------
A setter method is used to modify (update) the value of a private attribute.
It can also validate the new value before updating it.

Syntax:
    def set_attribute(self, value):
        self.__attribute = value


Advantages:
-----------
• Provides controlled access to private data.
• Allows data validation before modification.
• Protects data integrity.
• Implements the principle of encapsulation.
"""


class Student:
    def __init__(self, marks):
        self.__marks = marks

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")


student = Student(85)

print(student.get_marks())  # Getter

student.set_marks(95)  # Setter
print(student.get_marks())


"""
Getter and Setter using @property and @<property_name>.setter

Instead of writing separate get_ and set_ methods, Python provides the @property decorator 
to create a getter and @<property_name>.setter to create a setter. This is the Pythonic way 
of implementing encapsulation.
"""

class Student:
    def __init__(self, name):
        self.__name = name

    # Getter
    @property
    def name(self):
        return self.__name

    # Setter
    @name.setter
    def name(self, value):
        if value.strip() != "":
            self.__name = value
        else:
            print("Name cannot be empty.")

s = Student("Ishwar")

print(s.name)      # Calls Getter

s.name = "Rahul"   # Calls Setter
print(s.name)