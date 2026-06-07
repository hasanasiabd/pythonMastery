
# Iterator vs Iterable

List = [1,2,3,4,5,"Hasan","Ismail"]

# for i in List:
#     print(i)

x = iter(List)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(next(x))
print(next(x))
print(next(x))