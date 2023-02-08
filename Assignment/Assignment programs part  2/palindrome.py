s = input("Enter a string")
rev = s[::-1]
print(rev)
if rev == s:
    print("The given string is palindrome")
else:
    print("Not a palindrome string")
