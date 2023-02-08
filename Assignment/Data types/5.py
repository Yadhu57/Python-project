# 5.	Extend nested list by adding the sublist
# # sub list to add
# sub_list = ["h", "i", "j"]
# Expected Output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
for i in sub_list:
    list1[2][1][2].append(i)
print(list1)