#write a code showing the difference between global and local variables
x=100
print("x=",x)
def aFunction():
    x=50
    print("local x=",x)
aFunction()
print("global x=",x)