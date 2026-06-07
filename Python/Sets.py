
# Duplicates Not Allowed
# Sets cannot have two items with the same value.

myset = {1,2,3,1,4,6,3,"3"}
print(myset)

print(len(myset))

Myset = {1,"hasan",False,20.5}
print(Myset)
Myset1 = {1,"hasan",True,20.5}
print(Myset1)


# Access Set Items
for i in myset:
    print(i)

print(2 in myset)


# Add Set Items

set = {1,2,3,1,4,6,3,"3"}
set.add("hasan")
print(set)


# set update()

Set = {"Rased", "Mahadi", "Nazmul", "Masum", "Tufayel", "Tuhin", "Hasnat", "Hasan", "Hossain", "Abdullah", "Jaber"}
Set.update({"Arif", "Habib"})
print(Set)
print(len(Set))
print(type(Set))

a = {"Arif", "Habib"}
b = [1,2]
a.update(b)
print(a)
print(len(a))
print(type(a))



# Remove Set Items
# Note: If the item to remove does not exist, remove() will raise an error.

set5 = {1,2,3,4,5}
set5.remove(3)
print(set5)


#  discard() method
# Note: If the item to remove does not exist, discard() will NOT raise an error.

set5.discard(7)
print(set5)
set5.discard(1)
print(set5)

# pop() method:
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

set6 = {1,2,3,4,5}
set6.pop()
print(set6)

# clear() method:


set6.clear()
print(set6)

# set7 = {1,2,3,4,5}
# del set7
# print(set7)



# loop set

set9 = {"Rased", "Mahadi", "Nazmul", "Masum", "Tufayel", "Tuhin", "Hasnat", "Hasan", "Hossain", "Abdullah", "Jaber"}
for nam in set9:
    print(nam)



# Join Sets

# Union
# The union() method returns a new set with all items from both sets.

Set1 = {"a","b","c"}
Set2 = {1,2,3,4,5}
Set3 = Set1.union(Set2)
print(Set3)


# update() method

# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

Set4 = {"a","b","c"}
Set5 = {1,2,3,4,5}
Set5.update(Set4)
print(Set5)


# Python - Set Exercises
# সেট এক্সারসাইজ করার জন্য নিচের লিংকে যাও:

a = "https://www.w3schools.com/python/python_sets_exercises.asp"
print(a)


