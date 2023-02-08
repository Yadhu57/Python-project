#  2. write a program for python function that takes a list of words and returns the longest one.
l1 = ["aa", 'bbbbbbbbbbb', 'ccccc', 'dddddd', 'eeeeeeee']
m= len(l1[0])
temp = l1[0]
for i in l1:
    if len(i) > m:
        m = len(i)
        temp = i
print("biggest word is:", temp)


