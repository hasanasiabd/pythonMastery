

# Inheritance
# Multiple Inheritance
# Multilevel Inheritance
# Hybrid And Hierarchical Inheritance

class baba:
    car = "BMW"
    Home = "Boro Bari"

class baba2:
    car1 = "Marsitis"
    Home1 = "Biling"

class baba3:
    car2 = "Ferari"
    SmartPhone = "iPhone"
class Kaka(baba,baba2,baba3):
    brokenMobail = ""
    BaggaBari = ""

K = Kaka()
print(K.car)
print(K.SmartPhone)
print(K.Home)
K.brokenMobail = 20
print(K.brokenMobail)



# Multilevel Inheritance

class baba:
    car = "BMW"
    Home = "Boro Bari"

class son1(baba):
    car1 = "Marsitis"
    Home1 = "Biling"

class son2(son1):
    car2 = "Ferari"
    SmartPhone = "iPhone"
class son3(son2):
    brokenMobail = ""
    BaggaBari = ""

S = son3()
print(S.car2)
