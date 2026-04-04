# print the list element using the while loop
num = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<len(num) :
    print(num[i])
    i+=1


# search for a number in tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100)
j = 0
n= int(input("enter the number which you want to search"))

while j<len(nums) :
    if (nums[j] == n):
        print("the number is found at index" , j)
    j+=1

    
