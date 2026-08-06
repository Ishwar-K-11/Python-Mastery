from abc import ABC, abstractmethod


class shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(shape):
    def __init__(self, l: int, b: int):
        self.l = l
        self.b = b

    def area(self) -> int:
        return self.l * self.b


class Circle(shape):
    def __init__(self, r: int):
        self.radius = r

    def area(self):
        return 3.14153 * self.radius * self.radius


# S1 = shape()  --> So here when you try to creat a object of the abstract class its gives type error

R1 = Rectangle(19, 15)
print(f"The area of Rectangle is: {R1.area()}")

C1 = Circle(20)
print(f"The area of circle: {C1.area()}")
