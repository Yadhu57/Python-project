# 3.Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
str1 = "Luminar"
dict1 = {}
for index in range (1, len(str1)+1):
    dict1.setdefault(index, str1[index-1])
    print(index, str1[index-1])
print(dict1)



# for counting the letters
# for i in str1:
#     dict1[i] = dict1.get(i, 0)+1
# print(dict1)
