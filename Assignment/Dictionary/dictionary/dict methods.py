# """clear() method"""
# print("clear() method")
# dict1 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict1)
# p =dict1.clear()
# print(dict1)
# print("\n")
#
# """copy() method"""
# print("copy() method")
# dict2 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict2)
# p=dict2.copy()
# print(p)
# print("\n")
#
# """dict.fromkeys() method"""
# print("dict.fromkeys() method")
# dict3 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict3)
# p = dict.fromkeys(dict3,22)
# print(p)
# print("\n")
#
# """dict.get() method"""
# print("dict.get() method")
# dict4 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict4)
# print(dict4.get("name"))
# print("\n")
#
# """dict,has_key()"""
# # dict5 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# #
#
# """dict.items() method"""
# print("dict.items() method")
# dict6 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict6)
# print(dict6.items())
# print("\n")
#
# """dict.keys() method"""
# print("dict.keys() method")
# dict7 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict7)
# print(dict7.keys())
# print("\n")
#
# """dict.setdefault() method""" #adding a new key value pair to a dictionary
# print("dict.setdefault() method ")
# dict8 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict8)
# print(dict8.setdefault("suii","CR7"))
# print(dict8)
# print("\n")
#
# """dict.update()"""
# print("dict.update() method")
# dict9 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict9)
# dict10 = {"institution":"Luminar","Qualification": "B.Tech"}
# print(dict10)
# dict9.update(dict10)
# print(dict9)
# print("\n")
#
#
# """dict.values() method"""
# print("dict.values() method")
# dict11 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict11)
# print(dict11.values())
# print("\n")
#
# """len() method"""
# print("len() method")
# dict12 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict12)
# print(len(dict12))
# print("\n")
#
#
# """popItem() method"""  #pops the last element in the dictionary
# print("popitem() method")
# dict13 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict13)
# P = dict13.popitem()
# print(P)
# print("\n")
#
# """pop() method""" #pops an element given the key
# print("pop() method")
# dict14 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# print(dict14)
# print(dict14.pop("name"))
# print("\n")

# """del() method"""
# dict15 = {"name":'jyothis', "age":22, "place":"kottarakara"}
# del dict15["name"]
# del dict15
# print(dict15)

"""replacing value"""
dict15 = {"name":'jyothis', "age":22, "place":"kottarakara"}
dict15["name"] ="sreehari"
print(dict15)