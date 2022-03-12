""" Sort the goven data
    one:10, two:20, three:30, four:50
"""
myData={"one":10,
        "two":20, "three":30, "four":50}
sortedData1=zip(myData.values(),myData.keys())
sortedData2=zip(myData.keys(),myData.values())
print(sorted(sortedData1))
print(sorted(sortedData2))
#interesting
myData["five"]=40
print(myData)