# Code for learning of class and instance varible


# Class varible
class Student:
    school = "SOE&T"
    Name = "PCCOE"


student1 = Student()
student2 = Student()

print(student1.school)
print(student2.school)


# So here above you can see that the varible school and Name can be accessed by any object
# So this is called as Class Varible


class School:
    def __init__(self, name: str):
        self.names = name


student4 = School("Jack")
student5 = School("Sam")

print(student4.names)
print(student5.names)

# self.name is a instance varible behave or store different valuse for different object
# or we can say different object defferent behaviour
