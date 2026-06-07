from bdb import Breakpoint

# Python While Loops

Hasan = 0
while Hasan < 5:
    print("Hasan 10 theka boro", Hasan)
    Hasan += 1


# Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      continue
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
      break
  print(x)

