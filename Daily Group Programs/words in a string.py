# program to find all words in a string which have less than 4 letters

sentence = input("Enter a sentence:")
words = sentence.split()
print(words)
result = [x for x in words if len(x)<4]
print(result)
