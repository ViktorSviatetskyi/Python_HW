import sys

try:
    foroperand = sys.argv[1]
except IndexError:
    foroperand = ' '

try:
    sooperand = sys.argv[2]
except IndexError:
    sooperand = "Zen_of_Python.txt"

for line in open(sooperand):
    if foroperand in line:
        print(line, end='')

