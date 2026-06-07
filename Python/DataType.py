# from idlelib.configdialog import changes

#variable
kodu ='hjuuuuuuuutiubnd  354684168416541'
print(kodu)

Hasan_mama = 'urfdtrsttui'
print(Hasan_mama)

Hasan = '01850653020'
print(Hasan)

name1 = 'Hasan'
print(name1)
name_2 = 'Uddin'
print(name_2)

# int type data
hablu = 420
print(hablu)
print(type(hablu))

# floatingt type data
guru = 34156465.64
print(guru)
print(type(guru))

# complax type data
guruji = 01850653020j
print(guruji)
print(type(guruji))


# str type data
your_name = "hablu"
print(your_name)
print(type(your_name))
my_name = "hasan"
print(my_name)
print(type(my_name))
print(my_name + your_name)
print(type(my_name + your_name))
print(my_name + " " + your_name)
print(type(my_name + " " + your_name))

# bool type data
Bool = True
print(Bool)
print(type(Bool))
Bool = False
print(Bool)
print(type(Bool))
x = 10
y = 20
print(x>y)
print(x<y)
print(x==y)
print(x!=y)

# str data formating
name = Hasan
x = 10
y = 20
print(f'my name is{name}')
print(f'my name is{name} & my super number is {x+y}')

#Binary Types (bytes)
hasanlist = [1,5,65,67,255,160]
b = bytes(hasanlist)
#b[0] = 10 not changes
print(b)
print(type(b))
print(type(hasanlist))

# Binary Types (bytearray)
b1 = bytearray(hasanlist)
print(b1)
print(type(b1))
print(type(hasanlist))
b1[0] = 10
print(b1[0])
print(type(b1[0]))

#None Type
x = None
print(x)
print(type(x))

#Sequence Type data
#List Type data
li = ["Hasan","Hossain","Abdullah","Abdur Rahman"]
print(li)
print(type(li))
li[3] = 'Ismail'
print(li)
print(type(li))
print(type(li[3]))

#Tuple Type data
tup = (20,52,645,689)
print(tup)
print(type(tup))
print(type(tup[3]))

#Range Type data
ran = range(10)
print(ran)
print(type(ran))
for i in range(10):
    print(ran[i])

