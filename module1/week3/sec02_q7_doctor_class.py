# Question 7:
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name:str, yob:int):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob
    
    @abstractmethod
    def describe(self):
        pass


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist:str):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f"{self.__class__.__name__} - Name: {self._name} - YoB: {self._yob} - Specialist: {self.specialist}")


if __name__ == "__main__":
    
    doctor1 = Doctor(name='doctorZ2023', yob=1981, specialist='Endocrinologists')
    assert doctor1._yob == 1981
    doctor1.describe()