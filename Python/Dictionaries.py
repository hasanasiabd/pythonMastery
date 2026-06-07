
studentinfo = {
    "Hasan": {
        "name": "Hasan",
        "email": "hasanasiabd@gmail.com",
        "Class" : 10,
        "Roll": 108,
        "District" : "Gazipur"
     },
    "Hossain" :{
        "name": "Hossain",
        "email": "hossainaasia@gmail.com",
        "Class" : 7,
        "Roll" : 35,
        "District" : "Gazipur"
    },
    "Year" : 1952

}
print(studentinfo["Hasan"]["District"])


## Accessing Items
print(studentinfo["Year"])


# method get()    There is also a method called get() that will give you the same result:

x = studentinfo.get("Hossain")
print(x)


# keys() method     The keys() method will return a list of all the keys in the dictionary.

p = studentinfo.keys()
print(p)

# values() method       The values() method will return a list of all the values in the dictionary.

v = studentinfo.values()
print(v)



## Change Dictionary Items
## Add Dictionary Items


studentinfo["Year"] = 1971
print(studentinfo["Year"])

# update() method
# The update() method will update the dictionary with the items from the given argument.

studentinfo.update({"Hossain":2013})
print(studentinfo["Hossain"])

## Remove Dictionary Items

studentinfo.pop("Hasan")
print(studentinfo)

studentinfo.popitem()
print(studentinfo)
del studentinfo["Hossain"]
print(studentinfo)

abc = {
    10 : 20,
    20 :40
}
abc.clear()
print(abc)


## Loop Dictionaries

studentinfo = {
    "Hasan": {
        "name": "Hasan",
        "email": "hasanasiabd12@gmail.com",
        "Class" : 10,
        "Roll": 108,
        "District" : "Gazipur"
     },
    "Hossain" :{
        "name": "Hossain",
        "email": "hossainaasia@gmail.com",
        "Class" : 7,
        "Roll" : 35,
        "District" : "Gazipur"
    },
    "Year" : 1952

}

for x in studentinfo:
    print(x)

for y in studentinfo.values():
    print(y)

for z in studentinfo.keys():
    print(z)

for items in studentinfo.items():
    print(items)


## Copy Dictionaries

A = studentinfo.copy()
print(A)

B = dict(studentinfo)
print(B)

# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	         Description
# clear()	         Removes all the elements from the dictionary
# copy()	         Returns a copy of the dictionary
# fromkeys()	     Returns a dictionary with the specified keys and value
# get()	             Returns the value of the specified key
# items()	         Returns a list containing a tuple for each key value pair
# keys()	         Returns a list containing the dictionary's keys
# pop()	             Removes the element with the specified key
# popitem()	         Removes the last inserted key-value pair
# setdefault()     	 Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()       	 Updates the dictionary with the specified key-value pairs
# values()	         Returns a list of all the values in the dictionary\



# Python - Dictionary Exercises
# ডিকশেনারী এক্সারসাইজ করার জন্য নিচের লিংকে যাও:

a = "https://www.w3schools.com/python/python_dictionaries_exercises.asp"
print(a)

# a = {'name' : 'John', 'age' : 20}
# b = {'name' : 'May', 'age' : 23}
# customers = {'c1' : a, 'c2' : b}
# for x, obj in customers.items():
#   print(x)