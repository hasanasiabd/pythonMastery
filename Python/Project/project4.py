
# Project 4: Text Based Adventure Game

Answer = input("তুমি কি এই গেমটি খেলতে চাও। [Yes,হ্যাঁ/No,না]: ")
Yes
if Answer == "Yes" or Answer == "হ্যাঁ":
    print("এই খেলায় স্বাগতম।")
    Answer = input("তুমি কি জঙ্গলে যেতে চাও নাকি গুহায়? [Forest,জঙ্গলে/Cave,গুহায়]:")
    if Answer == "Forest" or Answer == "জঙ্গলে":
        print("তুমি ক্ষুধার্ত বাঘ দেখতে পাও। বাঘ তোমাকে খেয়ে ফেলে। এখন তুমি খেলায় হেরে গিয়েছ।")
    elif Answer == "Cave" or Answer == "গুহায়":
        print("তুমি সামনে ভালুককে দেখেছো।")
        Answer = input("তুমি কি ভাল্লুকের সাথে যুদ্ধ করতে চাও নাকি দৌড়ে পালাতে চাও? [Fight,যুদ্ধ/Run,দৌড়]:")
        if Answer == "Fight" or Answer == "যুদ্ধ":
            print("ভাল্লুকটি অনেক শক্তিশালী তুমি খেলায় হেরে গেছো")
        else:
            print("তুমি বেঁচে গিয়েছো এবং খেলায় জিতে গিয়েছো।")
elif Answer == "No" or "না":
    print("খেলা বন্ধ হয়ে গেছে।")

