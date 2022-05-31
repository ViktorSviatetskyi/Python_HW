import random


def hi(a):
    print("Hi, %s" % a)

num = random.randint(0, 10)
# print(num)
name = input('Enter your name: ')
hi(name)

def dsf(b):
    try:
        b = int(b)
    except ValueError:
        print("I said NUMBER! What is not clear?")
    else:
        return int(b)

guessNum = dsf(input("Try to guess the number from 0 to 10 "))
dsf(guessNum)

usertry = 1
while usertry:
    if (guessNum > 10 or guessNum < 0):
        print("I said from 0 to 10. Shame!!!")
    elif num > guessNum:
        print("The intended number is greater")
    elif num < guessNum:
        print("The intended number is less")
    elif num == guessNum:
        usertry = 0
        print("You guessed!!!!!!")
        break
