def square_number(number):
    return number**2


def expanded_string(s):
    return s[::-1]


def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    return "Not palindrome"


def run_tests():
    # Тестирование функции square_number
    assert square_number(2) == 4, "Ошибка в функции square_number: на входе 2"
    assert square_number(0) == 0, "Ошибка в функции square_number: на входе 0"
    assert square_number(-3) == 9, "Ошибка в функции square_number: на входе -3"

    # Тестирование функции expanded_string
    assert expanded_string("hello") == "olleh", "Ошибка в функции expanded_string: 'hello'"
    assert expanded_string("") == "", "Ошибка в функции expanded_string: пустая строка"
    assert expanded_string("a") == "a", "Ошибка в функции expanded_string: 'a'"

    # Тестирование функции is_palindrome
    assert is_palindrome("radar") == "Palindrome", "Ошибка в функции is_palindrome: 'radar'"
    assert is_palindrome("hello") == "Not palindrome", "Ошибка в функции is_palindrome: 'hello'"
    assert is_palindrome("а роза упала на лапу Азора") == "Palindrome", "Ошибка в функции is_palindrome: 'а роза упала " \
                                                                        "на лапу Азора'"

    print("Все тесты пройдены успешно!")





