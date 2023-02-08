# #1.Reverse a tuple

a = ('a', 'b', 'c', 'd')
print(a[::-1])


#  2. tple =(1, 2, 40, 30, 20) access the value 20 from the tuple,
#  tple2 = (1, 2, 40, [10, 2, 30], (30, 20, 10)) remove repeated elements from the tuple

tple = (1, 2, 40, 30, 20)
print(tple[4])
tple2 = (1, 2, 40, [10, 2, 30], (30, 20, 10), 40,)
lst = list(tple2)
for i in lst:
    if lst.count(i) > 1:
        lst.remove(i)
# tple2 = tuple(lst)
print(lst)
print(lst[3][1])

print("--------------------------------")

# 3. check if all items in the tuple are same
print("\n")
b = (1, 1, 1, 2)

