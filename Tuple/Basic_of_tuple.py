# basic of tuple

tup = (1,2,3,4,5,6)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[2])


#Create empty tuple

tuple = ()
print(tuple)
print(type(tuple))


#tuple slicing
tuple1 = (2,4,6,8,10,12,14)
print(tuple1[1:6])
print(tuple1[:5])
print(tuple1[0:])
print(tuple1[::])
print(tuple1[0:len(tuple1)])