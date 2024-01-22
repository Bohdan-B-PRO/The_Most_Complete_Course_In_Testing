

def make_cube(num):
    return num**3


def repeat(x):
    if isinstance(x, str):
        return x * 3
    return x * 2


def create_powers(*args, p=2):
    return [i**p for i in args]


def reverse_number(num):
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num //= 10
    return reversed_num


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)




