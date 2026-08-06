# Create a class in which different functions are there to calculate and display the avergae marks of the student also the grade


class Student:
    def __init__(self, name: str, roll_no: int, mark: list[int]) -> None:
        self.Name = name
        self.roll = roll_no
        self.Marks = mark

    def Total_Marks(self) -> int:
        return sum(self.Marks)

    def averge(self) -> int:
        return sum(self.Marks) / len(self.Marks)

    def grade(self) -> None:

        print("Name of Student: ", self.Name)
        print("Roll Number: ", self.roll)

        avg = self.averge()
        if avg >= 90:
            print("A")
        elif avg >= 70:
            print("B")
        elif avg >= 50:
            print("C")
        else:
            print("D")


student1 = Student("Aniket", 20, [77, 56, 87, 99])
total = student1.Total_Marks()
avg = student1.averge()
student1.grade()


# Always keep in mind that the __init__ function never return anything mostly used to initialize a value
