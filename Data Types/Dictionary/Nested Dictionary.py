dict2 = {"students":{"yadhu" ,"akhil","arun"}, "Courses": {"python", "java","html"}}
print(dict2)
print(dict2["Courses"])
print(dict2)
a = dict2.get("Courses")
print(a)
b = dict2.keys()
print(b)
c = dict2.values()
print(c)
d = dict2.items()
print(d)
dict2["Ages"] = {22, 23, 24}
print(dict2)
dict2.update({"Courses": "php"})
print(dict2)
dict2.popitem()
print(dict2)
dict2.pop("Courses")
print(dict2)
dict2.copy()
print(dict2)
dict2.clear()
print(dict2)
