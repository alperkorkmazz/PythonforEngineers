myList=[x for x in range(1,11)]
print(myList)
myList=[[x for x in range(1,11)] for x in range(1,11)]
print(myList)
myList=[[x for y in range(1,11)] for x in range(1,11)]
print(myList)
myList=[[x*y for y in range(1,11)] for x in range(1,11)]
print(myList)