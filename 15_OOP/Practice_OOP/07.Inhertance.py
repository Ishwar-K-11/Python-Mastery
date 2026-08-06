# Let's Learn super() in Inheritance and in __init__()


"""
super() in Inheritance
The super() function is used to access the parent class's methods or constructor
from within the child class.

It is especially useful when both the parent and child classes have methods with
the same name (method overriding). Calling the method directly from the child
class executes the child's version. To execute the parent's version, use super().

This allows the child class to extend the parent's functionality instead of
completely replacing it.
"""


class Animal:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def bark(self):
        print("Animals bark")

    def sound(self) -> None:
        print(f"{self.name} Makes sound")


class Dog(Animal):
    def bark(self):
        super().bark()
        self.sound
        print(f"{self.name} is Barking")
        print(f"{self.age} is the age of {self.name}")


d1 = Dog("Lion", 12)
d1.bark()
d1.sound()


"""
Using super() with the __init__() Constructor

The super().__init__(brand) statement calls the constructor (__init__) of the
parent class (Vehicle) from the child class (Model).

Why do we use super().__init__()?
---------------------------------
    • It initializes the attributes of the parent class without rewriting the same code.
    • It ensures that the parent class constructor executes before the child class
      continues its own initialization.
    • It avoids code duplication and follows the principle of code reusability.
    • If the parent constructor contains important initialization logic, super()
      guarantees that it is executed.

 In this example:
    ----------------
    1. model("Figo", "Ford") creates an object of the child class.
    2. The child class constructor (__init__) is called.
    3. super().__init__(brand) invokes the parent class constructor.
    4. The parent constructor initializes self.brand and prints the vehicle details.
    5. Control returns to the child constructor.
    6. The child constructor initializes self.model and prints the model details.

 Execution Flow:
    ---------------
    model.__init__()
            │
            ▼
    super().__init__(brand)
            │
            ▼
    vehicle.__init__()
            │
            ▼
    Initializes 'brand'
            │
            ▼
    Returns to model.__init__()
            │
            ▼
    Initializes 'model'
"""


class vehical:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        print("\nThis is vehicle constructor")
        print(f"The Brand of the car is: {self.brand}")


class model(vehical):
    def __init__(self, model: str, brand: str) -> None:
        self.model = model
        super().__init__(brand)
        print("\nThis is model constructor")
        print(f"The model of the car is: {self.model}")


M1 = model("Figo", "Ford")
