# Creating a clss and its object

class Student:
    def set_details(self,n:str,s:str,r:int,g:str,m:int) -> None:
        self.name = n
        self.school = s
        self.roll = r
        self.gender = g
        self.mark = m


    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Stream or School: {self.school}")
        print(f"Roll Number: {self.roll}")
        print(f"The Gender of student: {self.gender}")
        print(f"Total Marks Obtained By the Student: {self.mark}")


student_1 = Student()
student_1.set_details("Hussy","SOE&T",88,"Male",89)
student_1.display()


# so Here You can print give the input of many student 
# it will take frist student input then then peform the print task if you privid the second student marks
# then the frist student marks will get override

student_2 = Student()
student_2.set_details("Mike","SOE&T",77,"Male",76)
student_2.display()





