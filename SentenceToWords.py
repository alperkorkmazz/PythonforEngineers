"""
1. Write a simple code that gets each words of the sentence
    'White board 2022 Mexico'
2. Capitalize the first letters of each parts
"""
#split method use parameter as seperator. default () is empty char
#list function converts each character to a list element and adds to the list
word= 'White Board 2022 Mexico'
word_separated=word.split()

print(word_separated)
print(list(word))
for i in word_separated:
    print(i , end="+\n")