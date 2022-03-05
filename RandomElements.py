"""
Create a list of 10 random numbers between 0-100.
Then, print them on the screen in sorted form
"""
import random
sampleList=[]
for i in range(10):
    sampleList.append(random.randrange(0,101))
sampleList.sort()
print(sampleList)
sampleList.reverse()
print(sampleList)
