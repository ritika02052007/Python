# print number form 1 to 100
for el in range (1,101,1) :
    print(el)


#print number from 100 to 1
for el in range(100,0,-1) :
    print(el)


#print the multiplication table of number
n = int(input("enter the number"))
for el in range (1,11,1) :
    print(el * n)


# pass statement 
for el in range (5) :
    pass
print("some useful work")


# wap to find the sum of first n numbers 
n =  int(input("enter the number"))
sum  = 0
for el in range (1,n+1,1) :
    sum += el
print(sum)


# wap to find the factorial of a number 
n = int(input("enter the number")) 
fact = 1
for el in range (1,n+1,1) :
    fact *= el
print(fact)