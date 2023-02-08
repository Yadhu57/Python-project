# 2. Write a python code to remove all the repeating letters from each words of a given sentence.
# Eg:
#    	i/p:Let’s google the pineapple
#  		o/p:Let’s gole the pineal

str1 = "Let’s google the pineapple"
words = str1.split() 
str2 = []
for i in words:
    #    print(i)
    l = ""
    for j in i:
        #        print(j)
        if j in l:
            continue
        else:
            l = l + j
    str2.append(l)
print(" ".join(str2))
