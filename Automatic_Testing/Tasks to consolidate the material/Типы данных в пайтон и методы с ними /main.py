def strings(name):
    print("Hello World!")
    print(f"Привет, {name}")


def integers(number_1, number_2):
    result = number_1 + number_2
    return result, result * 10


def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def booleans():
    while True:
        try:
            # Запрашиваем у пользователя ввод
            number = input("Введите число: ")

            # Пытаемся преобразовать введённое значение в int, если не получается - в float
            try:
                num = int(number)
            except ValueError:
                num = float(number)

            # Проверка на положительное, отрицательное число или ноль
            if num > 0:
                print(f"{num} - положительное число")
            elif num < 0:
                print(f"{num} - отрицательное число")
            elif num == 0:
                print(f"{num} - это ноль")

            break  # Выход из цикла, если число успешно обработано
        except ValueError:
            # Обработка ошибки, если ввод не является числом
            print("Вы ввели не число! Пожалуйста, попробуйте еще раз.")
            break


def fruits_generator():
    """ Функция-генератор, создающая список фруктов """
    return ["Apples", "Bananas", "Pineapples", "Kiwis", "Oranges"]


def add_type_list(func):
    """ Декоратор, добавляющий элемент в список, возвращаемый func """
    def wrapper(*args, **kwargs):
        fruit_list = func(*args, **kwargs)
        fruit = input("Какой фрукты Вы хотите добавить? ")
        fruit_list.append(fruit)
        print(*fruit_list, sep=", ")
    return wrapper


@add_type_list
def enhanced_fruits():
    """ Обернутая версия функции-генератора списка фруктов """
    return fruits_generator()


# Вызов функции strings()
# strings(input("Ведите Ваше имя: "))

# Вызов функции integers()
# print(*integers())

# Вызов функции celsius_to_fahrenheit()
# celsius = float(input("Видите температуру в градусах Цельсия для преобразования в градусы Фаренгейта: "))
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C ❄️ равно {fahrenheit}°F ❄️")

# Вызов функции booleans()
# test_number = int(input("Видите число: "))
# booleans()

# Вызов функции type_list()
# type_list()

# Вызываем функцию enhanced_fruits()
# enhanced_fruits()




