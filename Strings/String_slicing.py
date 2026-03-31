# str[starting_idx : ending_idx ] ending is not include

str1 = "Apna college"
print(str1[1:4])
print(str1[:4])  # same as [0:4]
print(str1[0:])  #same as [0:len(str1)]

#negative indexing 
print(str1[-3:-1])
print(str1[-12:]) # same as [-12 :len(str1)]