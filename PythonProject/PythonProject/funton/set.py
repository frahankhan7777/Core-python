set = {'a',1,'b',2,3,4,5,6,7,8,9,10}
print(set)
print("Before the function call:", set)

set.add(11)
print("After the function call:", set)

set.add("Hello")
print("After the function call:", set)

set.add(11)
print("After the function call:", set)

set.remove(11)
print("After the function call:", set)

#print(set[1])