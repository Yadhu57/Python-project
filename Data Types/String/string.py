st1 = "hello"
st2 = 56
print(st1 + str(st2))  # str() is used to convert int to string

print(len(st1))  # len() used to find the length of a string

#looping through strings
index = 0
while index < len(st1):
    letter = st1[index]
    print(index, letter)
    index = index + 1

# find()
# find() returns -1 if substring not found
print(st1.find("e"))

#replace()

str1 = "hello welcome"
print(str1.replace('welcome','everyone'))
