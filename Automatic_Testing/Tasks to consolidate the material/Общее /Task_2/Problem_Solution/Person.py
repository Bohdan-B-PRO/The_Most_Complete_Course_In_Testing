class Person:

    def __init__(self, name):
        self.name = name

    def display_info(self):
        pass


class Student(Person):

    def __init__(self, name, student_ID_number):
        super().__init__(name)
        self.student_ID_number = student_ID_number

    def display_info(self):
        info = f"Имя студента: {self.name}\nНомер студенческого билета: {self.student_ID_number}"
        return info


class Teacher(Person):

    def __init__(self, name, major, years_of_experience):
        super().__init__(name)
        self.major = major
        self.years_of_experience = years_of_experience

    def display_info(self):
        info = f"Имя преподавателя: {self.name}\nПредмет, который ведёт преподаватель: {self.major}\nСтаж преподавателя: {self.years_of_experience}"
        return info


students = Student("Иван", "ID - 123321")
students_info = students.display_info()
print(students_info)

teachers = Teacher("Анна Васильевна", "Математика", 10)
teachers_info = teachers.display_info()
print(teachers_info)
