# waf to print the length of the list

def print_len (list1) :
    print(len(list1))

list1 = ["apna" ,"college" ,"hello" ,"world"]
print_len(list1)


# waf to print the elements of a list in a single line

def print_ele(list2) :
    for el in list2 :
        print(el , end = " ")

list2 = [12,34,23,56,78]
print_ele(list2)