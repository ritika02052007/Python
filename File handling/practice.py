# create a new file and "practice.txt" and add the some content

f = open("practice.txt" ,"w")
f.write("hii everyone \n we are learning file i/o using \n python i like programming in python")
f.close()


# wap that replace all occurence of "python" with "java" in above file
with open("practice.txt" ,"r") as f :
    data = f.read()
new_data = data.replace("python","java")
print(new_data)
with open ("practice.txt" ,"w") as f :
    f.write(new_data)


# search if the word "learning" exists in the file or not.
with open("practice.txt" ,"r") as f :
    data = f.read()
    if (data.find("learning") != -1) :
        print("found")
    else :
        print("not found")
