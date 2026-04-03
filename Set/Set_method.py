# set method

collection = set()  # create an empty set

collection.add(1)
collection.add(2)
collection.add(3)
collection.add(3)
print(collection)

collection.remove(3)  # use the remove method
print(collection)

collection.add(3)  # store multiple type value
collection.add("radha")
collection.add("a")
collection.add(123.45)
collection.add((1,2,3))
print(collection)

print(len(collection))  # it is used to print the length of set

collection.clear()  # clear all the set value
print(collection)   
print(len(collection))

collection = {"hello","apna college","world","coding","python"}
print(collection.pop())  # pop the last element of the set
print(collection.pop())

# union and intersection method
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,1}
print(set1.union(set2))
print(set1.intersection(set2))
