"""
Данный декоратор будет кешировать результат выполнения функции и при повторном вызове функция должна брать
значение из кеша, а не вычислять его по новой. Тесты нужно провести на какой-то тяжелой функции, выполнение
которой будет занимать какое-то время, чтобы была видна разница при повторных вызовах.
"""

from functools import wraps


def casher(function):
    cash = {}

    @wraps(function)
    def wrapper(*args):
        nonlocal cash
        if cash.get(args):
            print(f'For {"".join(map(str, args))} cashed')
            return cash[args]
        else:
            res = function(*args)
            cash[args] = res
            return res
    return wrapper


@casher
def heavy_def(degree):
    # global i   #####Тут Pycharm пропонує зробити глобальну перемінну, але я щось не до кінця зрозумів для чого :(
    for i in range(10 ** degree):
        i += 1
    return i


if __name__ == "__main__":
    print(heavy_def(7), '\n')
    print(heavy_def(8), '\n')
    print(heavy_def(7), '\n')
    print(heavy_def(8), '\n')

