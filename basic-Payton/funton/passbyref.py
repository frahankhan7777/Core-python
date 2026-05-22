def changeList(list):
    list.append(4)
    print("Inside the function:", list)


list =[1,2,3,4,5,6,7,8,9,10]
print("Before the function call:", list)
changeList(list)
print("After the function call:", list)