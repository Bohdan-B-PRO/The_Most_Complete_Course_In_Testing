import math
import random
from forex_python.converter import CurrencyRates
import string
import time

# Создаем объект для работы с курсами валют
currency_rates = CurrencyRates()


def currency_calculator(from_currency, to_currency):
    """
    Конвертирует сумму из одной валюты в другую.
    :param from_currency: Исходная валюта
    :param to_currency: Целевая валюта
    """
    try:
        # Получаем курс обмена между двумя валютами
        rate = currency_rates.get_rate(from_currency, to_currency)
        if rate == 0:
            print("Ошибка: курс валюты не может быть равен нулю.")
            return
        print(f"Курс {from_currency} к {to_currency}: {rate}")
    except Exception as e:
        print(f"Произошла ошибка при конвертации валют: {e}")


def factorial(number):
    """
    Вычисляет факториал заданного числа.
    :param number: Число для вычисления факториала
    """
    try:
        print(f"Факториал числа {number}: {math.factorial(number)}")
    except ValueError:
        print("Ошибка: факториал не может быть вычислен для отрицательного числа.")
    except Exception as e:
        print(f"Произошла ошибка при вычислении факториала: {e}")


def is_prime(number):
    """
    Проверяет, является ли число простым.
    :param number: Число для проверки
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def password_generator():
    """
    Генерирует случайный пароль.
    """
    character_count = random.randint(3, 250)
    password_characters = string.digits + string.punctuation + string.ascii_letters
    random_subset = random.sample(password_characters, character_count)
    return "".join(random_subset)


def countdown_timer(minutes):
    """
    Таймер обратного отсчета.
    :param minutes: Время в минутах для таймера
    """
    try:
        seconds = minutes * 60
        while seconds:
            mins, secs = divmod(seconds, 60)
            timer = "{:02d}:{:02d}".format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            seconds -= 1
        print("Время вышло!")
    except Exception as e:
        print(f"Произошла ошибка в таймере: {e}")


def main_menu():
    """
    Основное меню программы для выбора действий пользователем.
    """
    print("Выберите действие:")
    print("1. Узнать курс валют")
    print("2. Вычислить факториал числа")
    print("3. Проверить, является ли число простым")
    print("4. Сгенерировать пароль")
    print("5. Таймер обратного отсчета")

    try:
        choice = input("Введите номер действия: ")
        if choice == '1':
            user_input = input("Введите две валюты (например, 'USD EUR'): ").split()
            currency_calculator(user_input[0], user_input[1])
        elif choice == '2':
            fact = int(input("Введите число для вычисления факториала: "))
            factorial(fact)
        elif choice == '3':
            number = int(input("Введите число для проверки на простоту: "))
            print(f"Число {number} простое: {is_prime(number)}")
        elif choice == '4':
            print("Сгенерированный пароль: ", password_generator())
        elif choice == '5':
            timer = int(input("Введите количество минут для таймера: "))
            countdown_timer(timer)
        else:
            print("Неверный выбор")
    except ValueError:
        print("Неверный ввод, пожалуйста, введите число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Запускаем меню
if __name__ == "__main__":
    main_menu()
