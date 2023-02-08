# 1.Write a Python program to print all unique values in a dictionary.
listofdict = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
setof_uvalues = set()
for i in listofdict:
    for value in i.values():
        setof_uvalues.add(value)
print(setof_uvalues)









# method 2
# dict1= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# ul = []
# for i in dict1:
#     ul.extend(list(i.values()))
# ul = set(ul)
# print(ul)
