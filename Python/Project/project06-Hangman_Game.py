
# Project 6: Hangman Game

word = "fan"
Chancse = 3
GuessAdd = []
Done = False

while not Done:
    for Letter in word:
        if Letter.lower() in GuessAdd:
            print(Letter, end = " ")
        else:
            print("_" , end = " ")

    Myguess = input(f"তোমার সুযোগ হল {Chancse} বার , অক্ষরটি অনুমান করো: ")
    GuessAdd.append(Myguess.lower())
    if Myguess.lower() not in word.lower():
        Chancse -= 1
        if Chancse == 0:
            break

    Done = True
    for Letter in word:
        if Letter.lower() not in GuessAdd:
            Done = False

if Done:
    print(f"বাহ, তুমি খেলা জিতে গেছো।, শব্দটি ছিল {word}")
else:
    print("তুমি হেরে গিয়েছ।")
