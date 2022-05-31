#Давайте попробуем реализовать простую игру «угадай число».
#Пока что, для простоты, мы установим некоторое фиксированное число,
#которое пользователь должен угадать. Программа должна поприветствовать
#игрока, и попросить его ввести произвольное число. После чего программа сравнит
#его с тем, что мы записали и должна нам выдать 3 вида сообщений:
#- Загаданное число меньше.
#- Загаданное число больше.
#- Вы угадали!

num = 22
print("Enter your name")
name = input()
print("Hi, ", name)
print("Try to guess the number")
guessNum = int(input())

if num > guessNum:
    print("The intended number is greater")
elif num < guessNum:
    print("The intended number is less")
elif num == guessNum:
    print("You guessed!!!!!!")
