"""
setdefault():
-------------
If key is in the dictionary, return its value.
If not, insert key with a value of default and return default.
default defaults to None.

"""
str1 = 'Luminar'
#print("The given string is :",str1)
dict1 = {}
for index in range (1,len(str1)+1): #1, 7+1 = 1, 8
    #print(index)
    dict1.setdefault(index,str1[index-1])
    #print(index-1)
    # print(str1[index-1])
    # print(index,str1[index-1])
print("The corresponding dicitonary of the given string is :",dict1)