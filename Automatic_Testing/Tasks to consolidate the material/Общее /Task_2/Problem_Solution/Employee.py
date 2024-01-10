class Employee:

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Имя: {self.name}, Должность: {self.position}, Зарплата: {self.salary}")


# Создание экземпляра класса
my_employee = Employee("Куня", "ТОП-Менеджер центра ДНК", "1000000$")

# Вывод информации о сотруднике в консоль
my_employee.display_info()



