# open and read the file
f = open("demo.txt" ,"r")
data = f.read()
print(data)
f.close()

# read the file content line by line
f = open("demo.txt", "r")
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close()


# create and write the file content
f = open("sample.txt" ,"w")
f.write("hello world")
f.close()


# append the content in the existing file
f = open("sample.txt" ,"a")
f.write("\n now i am learning python")
f.close()