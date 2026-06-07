
# Project 3: Number Guessing Game With Limited Attempts

import random

RandomNumber = random.randrange(1,500)

UserImport = int(input("Guess the number: "))

if RandomNumber < UserImport:
    print(RandomNumber)
    print("The number is too high.")
elif RandomNumber > UserImport:
    print(RandomNumber)
    print("The number is too low.")
else:
    print(RandomNumber)
    print("Yes, you matched the number.")
