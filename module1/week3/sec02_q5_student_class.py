# Question 5:
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f"{self.__class__.__name__} - Name: {self._name} - YoB: {self._yob} - Grade: {self.grade}")

if __name__ == "__main__":
    
    student1 = Student(name="studentZ2023", yob=2011, grade="6")
    assert student1._yob == 2011
    student1.describe()

#Q5: A