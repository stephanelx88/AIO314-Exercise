# Question 8:

from sec02_q7_doctor_class import Doctor
from sec02_q5_student_class import Student, Person
from sec02_q6_teacher_class import Teacher



class Ward:
    def __init__(self, name:str):
        self.__name = name
        self._list_people = []

    def add_person(self, person:Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        doctors = [person for person in self.__listPeople if isinstance(person, Doctor)]
        
        return len(doctors)

if __name__ == '__main__':
    
    ward1 = Ward(name='Ward 1')
    student1 = Student(name="studentA", yob=2010, grade="7")
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinolgist")
    ward1.add_person(doctor1)
    assert ward1.count_doctor() == 1
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologist")

    ward1 = Ward(name='Ward1')
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    print(ward1.count_doctor())


# Q8: C