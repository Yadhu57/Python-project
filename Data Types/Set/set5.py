# 4. Remove items from set1 that are not common to both set1 and set 2
set1 = {2, 4, 6, 8, 10, 11, 12, 13, 14}
set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1 = set1 & set2
print(set1)