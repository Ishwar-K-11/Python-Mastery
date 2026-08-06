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