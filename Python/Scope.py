
a = 40
b = 50   #Global Scope

def myfunc():
    x = 100
    print(x)   #Local Scope
    print(a)

myfunc()