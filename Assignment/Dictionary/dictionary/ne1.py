dict1 = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d2 ={}
for key,values in dict1.items():
    d2[values]  = [key]
else:
    d2[values].append(key)
print(d2)