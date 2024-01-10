class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


student1 = Student("Иван", 20, [85, 90, 92, 78, 89])
average = student1.average_grade()
print(f"Средний балл студента {student1.name}: {average}")
