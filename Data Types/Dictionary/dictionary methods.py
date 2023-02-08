dict1 = {"name": "yadhu", "Age": 21, "course": "python"}
print(dict1["course"])
print(dict1.get("name"))
print(dict1.values())
print(dict1.keys())
print(dict1.items())

dict1["Age"] = 20
print(dict1)
dict1.update({"Age": 21, "course": "Java"})
print(dict1)

dict1.update({"place": "Eranakulam"})
print(dict1)

dict1.pop("place")
print(dict1)

dict1.popitem()
print(dict1)