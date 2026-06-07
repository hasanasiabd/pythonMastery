# Project 5: Ludo Dice Roller

import random

লুডু = True

while লুডু:
    print(random.randint(1,6))
    খেল = input("তুমি কি আবার গুটি চালাতে চাও। [Y/N]:")
    if খেল == "Y":
        continue
    else:
        print("খেলা শেষ")
        break
