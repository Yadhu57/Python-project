import json  # json- javascript object notation

# json
dict1 = '{"name": "abcdefgh", "address": "ijklmno"}'
print(type(dict1))

# converting json  to python
y = json.loads(dict1)
print(type(y))
#
# # converting json to python
# json.dump(y)
# print(type(y))
print(dir(json))