import re

str1 = 'class will start at 10am'
s = re.search('^class.*10am$',str1)
print(s)
if s:
    print('Find')
else:
    print('Not Find')

# Split() method

str2 = 'class will start at 10am'
s1 = re.split(' ', str2)
print(s1)

s3 = re.split('a', str2)
print(s3)