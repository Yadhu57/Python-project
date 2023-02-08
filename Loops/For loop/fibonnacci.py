# a = 0
# b = 1
# c = 0
# for i in range(10):
#     print(a, end=' ')
#     sum = a + b
#     a = b
#     b = sum
#     c += 1




# method  2
a,b=0,1
print(a)
print(b)
for i in range(10):
    c = a + b
    print(c)
    a, b = b, c