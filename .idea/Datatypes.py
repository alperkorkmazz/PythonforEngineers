"""
Find the Ascii numbers of each character in the expression 'Hello World. I am 07.'
ord(x) function finds the ascii value of the given character paramater
"""

word='Hello World. I Am 07. Extra-ü-ö-ä'
for x in word:
    print("Letter: ",x, " Ascii: ", ord(x), " Returned Chr: ", chr(ord(x)))