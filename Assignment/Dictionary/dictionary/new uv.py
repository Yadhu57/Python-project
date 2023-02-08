dic = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
ul = []
for i in dic:
    ul.extend(list(i.values()))
ul = set(ul)
print(ul)