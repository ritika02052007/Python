# q.1 store following word meaning in a python dictionary
# table :"a piece of furniture" ,"list of facts & figures"
# cat : "a small animal"  

dictionary ={
     "table " :["a piece of furniture" ,"list of facts & figures"],
     "cat " :"a small anima"
}
print(dictionary)



# q.2. wap to enter marks of 3 subject from the user and stote them in a dictionary .start with an empty dictionary and add one by one .use subject name as key and marks as value

marks = {} 
x = int(input("enter physics marks :"))
marks.update({"phy" : x})

y = int(input("enter chemistry marks :"))
marks.update({"chem" : y})

z = int(input("enter math marks :"))
marks.update({"math " :z})

print(marks)