# Let's Learn Inheritance

class Animal:
    def __init__(self,name:str,age:int)->None:
        self.name = name 
        self.age = age

    def sound(self)->None:
        print(f"{self.name} Makes sound")

class Dog(Animal):
    def bark(self):
        self.sound
        print(f"{self.name} is Barking")
        print(f"{self.age} is the age of {self.name}")


d1 = Dog("Lion",12)
d1.bark()
d1.sound()

