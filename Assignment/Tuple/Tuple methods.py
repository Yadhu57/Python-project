tupe1 = (5, 4, 6, 1, 2, 3, 0)
print("length:", len(tupe1))
print("maximum:", max(tupe1))
print("minimum:", min(tupe1))
print(all(tupe1))
print("sorted:", sorted(tupe1))
print("sum=", sum(tupe1))

# Enumerate
names = ['abhi', 'akhil', 'arun']
ages = [20, 21, 22]
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
