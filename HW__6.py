"""Давайте сделаем еще ряд улучшений в игре. Сейчас интервал, в котором игра
«загадывает» число, зашит в программу. Хотелось бы разрешить и это неудобство.
Итак, требуется передать верхнюю и нижнюю границу диапазона через параметры
командной строки. При этом иметь возможность и не задавать эти параметры извне.
В таком случае берем значения по умолчанию."""

import random
import sys

# args = {
#     'foroperand': sys.argv[1],
#     'sooperand': sys.argv[2]
# }


def checknum(num):
    if not num.isdigit():
        raise ValueError(f"[{num}] must be a number!!!")
    else:
        return int(num)


try:
    foroperand = checknum(sys.argv[1])
except IndexError:
    foroperand = 0

try:
    sooperand = checknum(sys.argv[2])
except IndexError:
    sooperand = 10


def hi(a):
    assert a, "Name is empty"
    print("Hi, %s" % a)


def checkguessnum(guessnum):
    guessnum = checknum(guessnum)
    if guessnum > sooperand or guessnum < foroperand:
        print(f"I said from {foroperand} to {sooperand}. Shame!!!")
        return
    else:
        return guessnum


def guessnumber(a, b):
    num = random.randint(a, b)
    while True:
        nn = checkguessnum(input(f"Try to guess the number from {a} to {b} "))

        if nn is None:
            break
        else:
            if num > nn:
                print("The intended number is greater")
                continue
            elif num < nn:
                print("The intended number is less")
                continue
            elif num == nn:
                print("You guessed!!!!!!")
                break


if __name__ == "__main__":
    hi(input('Enter your name: '))
    guessnumber(foroperand, sooperand)
