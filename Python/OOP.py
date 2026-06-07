
## Object-Oriented Programming (OOP)

# 1. Class & Object    ## Class & Object File
# 2. Inheritance       ## Inheritance File
# 3. Abstraction
# 4. Encapsulation
# 5. Polymorphism

class info:
    def Hablu(self,name,age):
        print(f"{name} is {age} years old")

H = info()
H.Hablu("Hasan",18)
H.Hablu("Hosain",13)
H.Hablu("Homayra",5)

class info2:
    def __init__(self,name,Number):
        print(f"My name is {name} & my Number is {Number}")

H = info2("Hasan",185066532020)


class ClassName:
    def InstanceMethod(self):   ## [self] Parameter
        print("This is Instance method")

    @classmethod
    def ClassMethod(cls):  ## [cls] Parameter
        print("This is class method")

    @staticmethod
    def StaticMethod():      ## No [Parameter]
        print("This is Static method")


p1 = ClassName()    ## [object]
# InstanceMethod
p1.InstanceMethod()         ## p1.ClassMethod()-[object]  , ## ClassName().ClassMethod()

# ClassMethod
ClassName.ClassMethod()    ## ClassName.ClassMethod() , ## p1.ClassMethod()-[object] , ## ClassName().Classmethod()

# StaticMethot
ClassName().StaticMethod()  ## ClassName.StaticMethod() , ## p1.StaticMethod()-[object] , ## ClassName().StaticMethod()



## 3. Abstraction
#[]

## 5.Polymorphism

class Vehicle:
    def __init__(self,Model,Brand,Component):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component

class Car(Vehicle):
    pass

class Plane(Vehicle):
    pass

c = Car("TRE25","BMW","Component1")
p = Plane("HGT58","Get8F","All Component")
print(c.Model)
print(p.Brand)


## 4. Encapsulation

class INFO:
    def info(self,Name,fatherName):
        self.__Name = Name
        self.__fatherName = fatherName
        print(self.__Name)   #Inside the class

i = INFO()
j = i.info("Hasan","Mohi uddin")  # No change (__)  -##Encapsulation
# print(i.__Name)

