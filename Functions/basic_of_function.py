# basic of function

# make a function to calculate sum of two number
def cal_sum(num1,num2) :
    sum = num1 +num2
    print(sum)
a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
cal_sum(a, b)


# Make a function to print hello any number of time 
def print_hello() :
    print("Hello")

print_hello()
print_hello()


# write a function to calculate average of three number
def aveg (a, b, c) :
    ave = (a+b+c) /3
    print(ave)

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = int(input("Enter the third number"))

aveg(a,b,c)


# default parameter 

def cal_product(a=1,b=2) :
    print(a*b)

cal_product()
def_product(3,5)