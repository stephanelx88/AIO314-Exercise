class Ward:
    def __init__(self, name, citizens):
        self.name = name
        self.citizens = []

    def add_person(self, person):
        self.citizens.append(person)

    def describe(self):
        print(f"{self.__class__.__name__}: {self.name}")
        for citizen in self.citizens:
            citizen.describe()

    def count_doctors(self):
        doctors = [citizen for citizen in self.citizens if isinstance(citizen, Doctor)]
        
        return len(doctors)

    def sort_age(self):

        self.citizens.sort(key=lambda citizen: citizen.yob, reverse=True)

    def compute_average(self):

        teacher_yob = [citizen.yob for citizen in self.citizens if isinstance(citizen, Teacher)]
        
        return int(sum(teacher_yob) / len(teacher_yob))



class Student:
    def __init__(self, name, yob, grade):
        self.name = name
        self.yob = yob
        self.grade = grade

    def describe(self):
        print(f"{self.__class__.__name__} - {self.name} - YoB: {self.yob} - Grade: {self.grade}")
        

    
class Doctor:
    def __init__(self, name, yob, specialist):
        self.name = name
        self.yob = yob
        self.specialist = specialist

    def describe(self):
        print(f"{self.__class__.__name__} - {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")
        


class Teacher:
    def __init__(self, name, yob, subject):
        self.name = name
        self.yob = yob
        self.subject = subject

    def describe(self):
        print(f"{self.__class__.__name__} - {self.name} - YoB: {self.yob} - Subject: {self.subject}")
        


if __name__ == '__main__':
    ward1 = Ward('My Thoi', [])

    # Citizens in My Thoi Ward
    student = Student(name='Nguyen', yob=2010, grade='7')
    teacher1 = Teacher('Vinh', 1969, 'Computer Science')
    teacher2 = Teacher('Luther', 1995, 'Physics')
    doctor1 = Doctor('Sneiden', 1945, 'Inner Medicine')
    doctor2 = Doctor('Trung', 1975, 'Therapist')

    people = [student, teacher1, teacher2, doctor1, doctor2]

    for person in people:
        ward1.add_person(person)

    ward1.describe()

    # Question 2c:
    print(f"\nNumber of doctors: {ward1.count_doctors()}")

    # Question 2d:
    ward1.sort_age()
    ward1.describe()

    # Question 2e:
    teacher_avg_yob = ward1.compute_average()
    print(f"\nAverage year of birth (teachers): {teacher_avg_yob}")