ch = input("Enter an alphabet")
if ch.isalpha():
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U":
        print(ch, " is a vowel")
    else:
        print(ch, "is a consonant")
else:
    print("please enter  an alphabet")
