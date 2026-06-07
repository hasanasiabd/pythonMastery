
# sadaro

HabiuMama = (1,2,"hasan","Hablu","ismail","nasir",25.5)

print(type(HabiuMama))
print(HabiuMama)

# Negative Indexing

print(HabiuMama[-2])
print(HabiuMama[-1])


# print(HabiuMama[:2])
# print(HabiuMama[:])

# Range of Indexes
print(HabiuMama[0:7])
print(HabiuMama[2:4])


# Update Tuples

HabiuMama = (1,2,"hasan","Hablu","ismail","nasir",25.5)

A = list(HabiuMama)
print(type(A))

A.append("gablu")
print(A)

HabiuMama = tuple(A)
print(HabiuMama)
print(type(HabiuMama))



# Unpack Tuples

fruits = ("apple", "banana", "cherry")

*a, b = fruits
print(a)
print(b)


# Loop Tuples

Bro = ("Rased","Mahadi","Nazmul","Masum","Tufayel","Tuhin","Hasnat","Hasan","Hossain","Abdullah","Jaber")

for i in Bro:
    print(i)

for x in range(len(Bro)):
    print(x)
    print(Bro[x])

y = 0

while y < len(Bro):
    print(Bro[y])
    y += 1



# Join Tuples
    # Join Two Tuples


fruits = ("apple", "banana", "cherry")
num = (1,2,3,4,5,6,7,8,9,10)

Two = fruits + num
print(Two)

# Multiply Tuples
Bro = ("Rased","Mahadi","Nazmul","Masum","Tufayel","Tuhin","Hasnat","Hasan","Hossain","Abdullah","Jaber")

i = Bro * 2

print(i)



# Tuple Methods

Bro = ("Rased","Mahadi","Nazmul","Masum","Tufayel","Tuhin","Hasnat","Hasan","Hossain","Abdullah","Jaber","hasan","hasan")

indexing = Bro.index("hasan")
print(indexing)

counting = Bro.count("hasan")
print(counting)


# Exercise
# টাপল এক্সারসাইজ করার জন্য নিচের লিংকে যাও:

a = "https://www.w3schools.com/python/exercise.asp?x=xrcise_tuples1"
print(a)

