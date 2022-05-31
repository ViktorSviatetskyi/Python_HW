import random

def hi(a):
    assert a, "Name is empty"
    print("Hi, %s" % a)


def Check(guessNum):
    if not guessNum.isdigit():
        print("I said NUMBER! What is not clear?")
        return
    else:
        guessNum = int(guessNum)
        if guessNum > 10 or guessNum < 0:
            print("I said from 0 to 10. Shame!!!")
            return
        else:
            return guessNum

num = random.randint(0, 10)
name = input('Enter your name: ')
hi(name)

while True:
    guessNum = input("Try to guess the number from 0 to 10 ")
    nn = Check(guessNum)

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
