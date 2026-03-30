# check the grade according to the marks
marks = int(input("Enter the marks :"))

if(marks >80 and marks <=100):
    print("You got 'A' grade")

elif(marks <80 and marks >70 ):
    print("You got 'B' grade")

elif(marks >60 and marks <70) :
    print("You got 'C' grade")

elif(marks >40 and marks <60):
    print("You got 'D' grade")

else :
    print("You are failed")