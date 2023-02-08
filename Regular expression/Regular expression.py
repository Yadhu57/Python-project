import re

# d = 'cat mat pat rat sat'
# a = re.findall('[^scr]', d)
# print(a)


d = 'cat mat pat rat sat 99988 9999'
a = re.findall('\d{3}', d)
print(a)

str = 'class will start at 10am'
s = re.search('\s', str)
print(s)
print(s.start())

s1 = re.search('\d', str)
print(s1.start())

s2 = re.search('python', str)     # return None when not matches
print(s2)
