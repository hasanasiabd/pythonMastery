#Python


#Lists
li = [50,60,10,15]
print(li)
print(type(li))
li[1] = 20
print(li)
print(type(li))

lis = ['Hasan','Hossain','Abdullah','Jaber']
print(lis)
print(type(lis))
lis[3] = 'Sakib'
print(lis)
print(type(lis))

list = [True, False, True, True, False]
print(list)
print(type(list))
list[3] = False
print(list)
print(type(list))



#Access List Items
Name = ['Hasan','Hossain','Abdullah','reerjy']
print(Name[1])
print(type(Name[1]))

#Change List Items
Name[3] = 'Jaber'
print(Name)
print(type(Name))
print(type(Name[3]))


#Add List Items

#append()
Name.append('Sakib')
print(Name)
print(type(Name))

#Insert
Name.insert(0,'Homayra')
print(Name)
print(type(Name))


#Remove List Items

# The remove() method removes the specified item.
Newlist = ['Hasan','Hossain','Abdullah','reerjy']
Newlist.remove('reerjy')
print(Newlist)
print(type(Newlist))

# The pop() method removes the specified index.
Newlist.pop(2)
print(Newlist)
print(type(Newlist))

# The del keyword also removes the specified index.   Age use # ...
del Newlist[1]
print(Newlist)
print(type(Newlist))


ANewlist = ['Hasan','Hossain','Abdullah',]

#The clear() method empties the list.
print(ANewlist)
ANewlist.clear()
print(ANewlist)
print(type(ANewlist))



# Loop Lists


# You can loop through the list items by using a for loop:
Looplist = ["Nusrat","Khadija","Atia","nayima","sayama"]

for sister in Looplist:
    print(sister)

#Use the range() and len() functions to create a suitable iterable.

for i in range(len(Looplist)):
    print(i)

# Print all items, using a while loop to go through all the index numbers

y = 0
while y < len(Looplist):
    print(Looplist[y])
    y += 1


# List Comprehension

num = [1,2,3,4,5]
double = [i * 2 for i in num]
print(double)

c = [i / 5 for i in num]
print(c)

# Sort Lists
 # List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
   # Sort the list alphabetically:

hasan = ['1,Hasan','2,Hossain','3,Abdullah']
hasan.sort()
print(hasan)


# Sort Descending
 # To sort descending, use the keyword argument reverse = True:

hasan.sort(reverse = True)
print(hasan)

# Sort the list alphabetically:

number = [10,13,0,5,6,7,1,2,4,3,9,8,12,11]
number.sort()
print(number)


# Sort Descending
 # To sort descending, use the keyword argument reverse = True:

number.sort(reverse = True)
print(number)

# Copy Lists

NUMBER = [1,2,3,4,5]
print(NUMBER)

NUMBER2 = NUMBER.copy()
print(NUMBER2)


# Join Lists

num1 = [1,2,3]
num2 = [4,5,6]
num3 = num1 + num2
print(num3)

print(num1)

num1.extend(num2)

print(num1)

#Python - List Methods
  # List Methods

     # Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list








