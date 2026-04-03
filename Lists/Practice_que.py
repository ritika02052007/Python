# q.1 wap to ask the user to enter names of their 3 favourite movie & store them in a list

movies =[]
movie1 = input("Enter first movie")
movie2 = input("Enter second movie")
movie3 = input("Enter third movie")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)

print(movies)


#q.2 wap to count the number of student with the "a" grade in the following list

grade = ["C","D","A","A","B","B","A"]
print(grade.count("A"))


# q.3 store the below value in the list and sort them

grades  = ["C","D","A","A","B","B","A"]
grades.sort()
print(grades)


#q.4 wap to check if a list contain a palindrome of elements.

list = [1,2,3,2,1]
list1 = list
list.reverse()
if (list == list1) :
    print("It is palindrome list")
else:
    print("It is not palindrome listn")