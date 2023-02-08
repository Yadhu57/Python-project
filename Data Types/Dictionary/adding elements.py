dict1 = {"Name": "Yadhu", "Age": 21, "Course": "python"}
print(dict1)
# dict1.update({"place": "Idukki"})
# print("updated:", dict1)
key = input("enter key:")
value = input("Enter the value")
dict1.update({key: value})
print("updated:", dict1)
