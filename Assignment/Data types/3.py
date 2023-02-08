# 3.Replace each special symbol with # in the following string
#   str1 = '/*Jon is @developer & musician!!'
#  o/p:    ##Jon is #developer # musician##

str1 = '/*Jon is @developer & musician!!'
str1 = str1.replace('/', '#').replace('*', '#').replace('!', '#').replace('@', '#').replace("&", "#")
print(str1)


# METHOD 2

# import string
# str2 = '/*Jon is @developer & musician!!!'
# symbols = string.punctuation
# for i in str2:
#     if i in symbols:
#         str2 = str2.replace(i, "#")
# print(str2)