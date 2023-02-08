# program to print characters from a string that are present at an even index number

str1 = input("Enter a string")
print("The string is:", str1)
l = len(str1)
print("Characters at even index are:")
for i in range(0, l, 2):
    print((str1[i]))